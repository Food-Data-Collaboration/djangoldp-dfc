"""This module is loaded by DjangoLDP core during setup."""

import os

MIDDLEWARE = []
INSTALLED_APPS = []

# NOTE: Package variables are prefixed DFC_XYZ

# Keycloak configuration
KEYCLOAK_URL = f"{os.getenv('KEYCLOAK_URL')}/realms/{os.getenv('KEYCLOAK_REALM')}/protocol/openid-connect/token"
KEYCLOAK_CLIENT_ID = os.getenv("KEYCLOAK_CLIENT_ID")
KEYCLOAK_CLIENT_SECRET = os.getenv("KEYCLOAK_CLIENT_SECRET")

# Dataservers that this platform caches data from.
DFC_DATASERVER_URLS = os.getenv("DATASERVER_URLS", "").split(",")
# Set to False to disable storing logs of dataserver imports in the database.
DFC_STORE_IMPORT_REPORTS = True

# Defines the default read scopes, if not overridden during the Discovery mechanism.
# TODO: ReadOrders and ReadProducts aren't implemented on the staging data-server, but should be included.
DFC_KEYCLOAK_READ_SCOPES = {"ReadEnterprise": "enterprises/"}

# Defines a mapping between models and scopes. A static binding that is consistent for all data-servers.
DFC_KEYCLOAK_MODEL_READ_SCOPES = {"dfc-b:Enterprise": "ReadEnterprise"}

LDP_RDF_CONTEXT = "https://cdn.startinblox.com/owl/dfc.jsonld"

MIDDLEWARE = ["data_food_consortium.middleware.DisbaleJWTMiddleware"]
