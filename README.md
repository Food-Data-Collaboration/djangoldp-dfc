# Data Food Consortium Proxy Application

The objective of this package is to provide DjangoLDP applications using it with all of the tools they need to run a Data Food Consortium (DFC) Proxy.

## Models

The model definitions provide a full implementation of the [DFC business ontology](https://raw.githubusercontent.com/datafoodconsortium/ontology/refs/heads/master/src/DFC_BusinessOntology.owl). The resulting viewset is able to perform CRUD operations on the ontology data, parsed and serialized in JSON-LD.

## Access to live data

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
