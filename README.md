# Data Food Consortium Proxy Application

The objective of this package is to provide DjangoLDP applications with all of the tools they need to run a Data Food Consortium (DFC) Proxy.

## Automated updates of live data

The model definitions provide a full implementation of the [DFC business ontology](https://raw.githubusercontent.com/datafoodconsortium/ontology/refs/heads/master/src/DFC_BusinessOntology.owl). The resulting viewset is able to perform CRUD operations on the ontology data, parsed and serialized in JSON-LD.

##  Access to live data

Each proxy operates as a cache of the data from one or several DFC sources. The package proposes a solution for supporting this cache out-of-the-box, using a management command that can be launched manually and via a cronjob.

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

### Automated updates of live data via webhook

Data-servers implementing the DFC specifications will transmit webhooks to the proxy server when a resource is updated or when the proxy server's permissions to access the resource have changed. That webhook is implemented by this package, so the maintainer of the proxy server doesn't need to do anything to set this up. For the data-server implementation, though, here is a description of the working flow:

1. an Enterprise has been modified (created, updated, deleted), or the permissions of a proxy application to access it have been changed by the enterprise user.
2. The data server sends a POST request to the proxy server on the path `/djangoldp-dfc/webhook/`. The body of the POST request indicates which the urlid and type of the affected object:

```json
{
    "@id": "https://data-server.cqcm.startinblox.com/api/dfc/enterprises/enterprise-1",
    "@type": "dfc-b:Enterprise"
}
```

The POST request will need to be accompanied by a token authenticated with the keycloak server.

3. The proxy server will authenticate the POST requests token with keycloak. It will respond with a `401` if it is unable to do so. If the token is valid but the host given with the `@id` does not match the authenticated client, it will respond with `403`.
4. The proxy server will match the `@type` given to the `rdf_type` configured on a model in this package. If it is unable to resolve the model it will respond `404`. If the model is known but it is not part of the caching standard, it will respond `400`. If the `@type` is OK, at this point the proxy server will respond 200 to the webhook request.
5. If only the `@id` and the `@type` were sent by the data-server, then the proxy server will make a `GET` request retrieve the full enterprise by following the urlid given.
6. If the requested resource responds `404` (because the permission has been revoked), the proxy server will delete the Enterprise from its' local database. Otherwise, the enterprise and connected models will be updated with the new data. If the enterprise model did not exist, a new Enterprise will be created.

## Contributing

### Maintenance of the ProductTypes data

The Product models (the children of AbstractProduct) are different _forms_ of Product based on their relationship to the supply chain. Product _type_ on the other hand refers to the type of product (e.g. bread, vegetable). The exhaustive list of valid values for this field comes from the [dfc-pt ontology](https://raw.githubusercontent.com/datafoodconsortium/taxonomies/refs/heads/main/productTypes.rdf), and accordingly in our implementation the field is a TextChoices field bound to the enum `data_food_consortium.enums.ProductType`.

The dfc-pt ontology will change over time, and this enum will need to be updated with new values. To make the process easier, this repository includes a management command that can be run with `python manage.py check_product_types`. The command will compare the latest version of the ontology to the defined values of the enumeration and will suggest changes to the enumeration based on any differences.
