"""This module is loaded by DjangoLDP core during setup."""

import os

MIDDLEWARE = []
INSTALLED_APPS = []

# Package variables are prefixed DFC_XYZ

# Keycloak configuration
DFC_KEYCLOAK_URL = f"{os.getenv('KEYCLOAK_URL')}/realms/{os.getenv('KEYCLOAK_REALM')}/protocol/openid-connect/token"
DFC_KEYCLOAK_CLIENT_ID = os.getenv("KEYCLOAK_CLIENT_ID")
DFC_KEYCLOAK_CLIENT_SECRET = os.getenv("KEYCLOAK_CLIENT_SECRET")

# Dataserver (resource server)
DFC_DATASERVER_URLS = ["https://data-server.cqcm.startinblox.com"]
# TODO: There are some questions around the scopes and their discovery.
# A discovery mechanism was proposed
# https://git.startinblox.com/projets/projets-clients/open-food-network/data-permissioning-module/-/issues/12#note_90778
DFC_KEYCLOAK_READ_SCOPES = {
    "ReadEnterprise": "/protected",
    "ReadOrders": "/protected",
    "ReadProducts": "/protected",
}
