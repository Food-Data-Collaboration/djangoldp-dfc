import requests

from django.conf import settings


def keycloak_is_configured():
    """Returns True if keycloak settings have been configured on the server."""
    return None not in [
        settings.DFC_KEYCLOAK_URL,
        settings.DFC_KEYCLOAK_CLIENT_ID,
        settings.DFC_KEYCLOAK_CLIENT_SECRET,
    ]


class KeycloakNotConfiguredException(Exception):
    pass


class KeycloakAuthenticationException(Exception):
    pass


class KeycloakClient:
    scopes = ""

    def __init__(self, scopes):
        if not keycloak_is_configured():
            raise KeycloakNotConfiguredException()
        self.scopes = scopes

    def get_access_token(self):
        payload = {
            "client_id": settings.DFC_KEYCLOAK_CLIENT_ID,
            "client_secret": settings.DFC_KEYCLOAK_CLIENT_SECRET,
            "grant_type": "client_credentials",
            "scope": self.scopes,
        }

        response = requests.post(settings.DFC_KEYCLOAK_URL, data=payload)

        if response.status_code == 200:
            return response.json()["access_token"]

        raise KeycloakAuthenticationException(
            f"Failed to get access token: {response.text}"
        )
