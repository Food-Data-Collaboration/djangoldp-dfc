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

To test your configuration, please run the command `python manage.py refresh_from_cache`.

### Automated updates of live data

In the current version of this package, the recommended approach to synchronising the proxy to its' dataserver federation is to schedule the `refresh_from_cache` command to run (for example) daily or weekly.

## Contributing

### Maintenance of the ProductTypes data

The Product models (the children of AbstractProduct) are different _forms_ of Product based on their relationship to the supply chain. Product _type_ on the other hand refers to the type of product (e.g. bread, vegetable). The exhaustive list of valid values for this field comes from the [dfc-pt ontology](https://raw.githubusercontent.com/datafoodconsortium/taxonomies/refs/heads/main/productTypes.rdf), and accordingly in our implementation the field is a TextChoices field bound to the enum `data_food_consortium.enums.ProductType`.

The dfc-pt ontology will change over time, and this enum will need to be updated with new values. To make the process easier, this repository includes a management command that can be run with `python manage.py check_product_types`. The command will compare the latest version of the ontology to the defined values of the enumeration and will suggest changes to the enumeration based on any differences.
