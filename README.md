# Data Food Consortium Proxy Application

The objective of this package is to provide DjangoLDP applications with all of the tools they need to run a Data Food Consortium (DFC) Proxy.

## Installation

Add to your `dependencies` and `ldppackages` in `settings.yml`. Make sure that this package is installed before DjangoLDP-Account (if you are using it), or else the middleware settings may conflict.

## Automated updates of live data

The model definitions provide a full implementation of the [DFC business ontology](https://raw.githubusercontent.com/datafoodconsortium/ontology/refs/heads/master/src/DFC_BusinessOntology.owl). The resulting viewset is able to perform CRUD operations on the ontology data, parsed and serialized in JSON-LD.

##  Access to live data

Each proxy operates as a cache of the data from one or several DFC sources. The package proposes a solution for supporting this cache out-of-the-box, using a management command that can be launched manually and via a cronjob. The management command (`refresh_from_cache`) will essentially scrape the views by scope as configured, but once this process has been completed once the cache can fallback to a webhook system as described below.

### Configuration

To use live data with your application you will need to configure Keycloak. Before using the features described please set the following environment variables:
* `KEYCLOAK_URL`
* `KEYCLOAK_CLIENT_ID`
* `KEYCLOAK_CLIENT_SECRET`

To configure the dataservers in the federation, please override the following in DjangoLDP settings:
* `DFC_DATASERVER_URLS`. Use base URLs, for example `http://localhost:8001/`.
* `DFC_KEYCLOAK_READ_SCOPES`. The scopes to scrape (e.g. `ReadEnterprise`). The available scopes are configured in your Keycloak Realm.

For the following settings, the default values should suffice.
* `DFC_KEYCLOAK_MODEL_READ_SCOPES`. Maps RDF classes from the DFC ontologies to the scopes required to read them.

To test your configuration and initialise data from the configured dataservers, please run the command `python manage.py refresh_from_cache`.

### Implementing Data-Server access for the cache refresh

All scopes of the spec are defined by [this document](https://cdn.startinblox.com/owl/dfc/taxonomies/scopes.jsonld). They are:
* `ReadProducts`
* `ReadOrders`
* `ReadEnterprise`
* `WriteOrders`
* `WriteProducts`
* `WriteEnterprise`

For each Read scope that you wish to support (i.e. from Products, Orders and Enterprises), you will need to create a GET endpoint to retrieve the associated information, serialized into JSON-LD with the classes and properties from the DFC standard. These endpoints should be authenticated with Keycloak, and only resources granted to the platform/proxy server should be returned to it, once authenticated. For more information consult the data permissioning specification associated to this network.

Optionally expose a view with your endpoint configurations at `/.well-known/dfc/`, a view which accepts a GET request and responds with a JSON document like so:
```json
{
    "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/scopes.rdf#ReadEnterprise": "/enterprises/",
    "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/scopes.rdf#ReadProducts": "/supplied_products/",
    "https://github.com/datafoodconsortium/taxonomies/releases/latest/download/scopes.rdf#ReadOrders": "/orders/"
}
```

If the resource server receives a 404 when requesting the above `.well-known` document, it will presume the default configuration is available, defined in the JSON structure above. The document defines the endpoints where data associated to a scope can be found (the configuration on ReadEnterprise defines where the resource server can retrieve instances of `dfc-b:Enterprise`.)

It's a good idea to paginate your data if there's a lot of it. If you include in the response the key `next`, the cache refresh will follow this link to continue importing data until `next` is not returned or is returned with the value `null`. Hence you can configure ReadEnterprise to use the url `https://myserver.com/enterprises/?limit=10`, responding in the body `next: https://myserver.com/enterprises/?limit=10&offset=10`. This example is inspired by the method of pagination known as limit-offset, supported by Django Rest Framework and DjangoLDP.

### Automated updates of live data via webhook

Data-servers implementing the DFC specifications will transmit webhooks to the proxy server when a resource is updated or when the proxy server's permissions to access the resource have changed. That webhook is implemented by this package, so the maintainer of the proxy server doesn't need to do anything to set this up. The documentation is included for the benefit of the data-server implementation, which uses the webhook.

A Postman collection has been created to accompany these docs which provides example events.

The webhook is called when one of three things happens:
1. a resource which the proxy has access to has been created or updated. In this case, the data-server should POST the serialization of the object to the webhook directly, using the `eventType` `"update"`. A PUT operation will be performed with the data given.
2. a resource which the proxy has access to has been deleted or permission to the object has been revoked. In this case, the data-server should POST the `@id` and `@type` of each resource _revoked_ in a list under the key `objects`. It should use the `eventType` `"revoke"`.
3. the proxy has had a scope permission given or revoked on the data-server (for a given enterprise). In this case, the `eventType` should be `"refresh"`. The `enterpriseUrlid` should be the `@id` of the enterprise which granted/revoked their data.

In all cases, the endpoint on the proxy server is `/djangoldp-dfc/webhook/`, and the request type is POST.

## Contributing

### Maintenance of the ProductTypes data

The Product models (the children of AbstractProduct) are different _forms_ of Product based on their relationship to the supply chain. Product _type_ on the other hand refers to the type of product (e.g. bread, vegetable). The exhaustive list of valid values for this field comes from the [dfc-pt ontology](https://raw.githubusercontent.com/datafoodconsortium/taxonomies/refs/heads/main/productTypes.rdf), and accordingly in our implementation the field is a TextChoices field bound to the enum `data_food_consortium.enums.ProductType`.

The dfc-pt ontology will change over time, and this enum will need to be updated with new values. To make the process easier, this repository includes a management command that can be run with `python manage.py check_product_types`. The command will compare the latest version of the ontology to the defined values of the enumeration and will suggest changes to the enumeration based on any differences.
