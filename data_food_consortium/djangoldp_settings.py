"""This module is loaded by DjangoLDP core during setup."""

import os

MIDDLEWARE = []
INSTALLED_APPS = []

# NOTE: Package variables are prefixed DFC_XYZ

# Keycloak configuration
KEYCLOAK_URL = f"{os.getenv('KEYCLOAK_URL')}/realms/{os.getenv('KEYCLOAK_REALM')}/protocol/openid-connect/token"
KEYCLOAK_CLIENT_ID = os.getenv("KEYCLOAK_CLIENT_ID")
KEYCLOAK_CLIENT_SECRET = os.getenv("KEYCLOAK_CLIENT_SECRET")

# Set to False to disable storing logs of dataserver imports in the database.
DFC_STORE_IMPORT_REPORTS = True

# Defines the default read scopes, if not overridden during the Discovery mechanism.
# TODO: ReadOrders and ReadProducts aren't implemented on the staging data-server, but should be included.
# TODO: Scopes could be configured per-dataserver by using the DataServer model.
DFC_KEYCLOAK_READ_SCOPES = {"ReadEnterprise": "enterprises/"}
DFC_REQUESTED_SCOPES_DOCUMENT = (
    "https://cdn.startinblox.com/owl/dfc/taxonomies/cqcm.jsonld"
)

LDP_RDF_CONTEXT = (
    "https://cdn.jsdelivr.net/gh/datafoodconsortium/ontology/context/context_2.0.0.json"
)
LDP_RDF_CONTEXT_V1 = "https://cdn.jsdelivr.net/gh/datafoodconsortium/ontology/context/context_1.16.0.json"

MIDDLEWARE = ["data_food_consortium.middleware.DisbaleJWTMiddleware"]

DATA_UPLOAD_MAX_MEMORY_SIZE = 5242880
