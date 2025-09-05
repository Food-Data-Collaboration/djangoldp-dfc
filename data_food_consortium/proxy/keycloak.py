import os
import requests

from authlib.jose import jwt as authlib_jwt
from authlib.jose.errors import JoseError

from django.conf import settings
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed


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
            # "client_id": settings.DFC_KEYCLOAK_CLIENT_ID,
            # "client_secret": settings.DFC_KEYCLOAK_CLIENT_SECRET,
            "client_id": "https://locavora-data-server-staging.nn.r.appspot.com/",
            "client_secret": "urvat4H59N3gye7OqP3JCfuMlwVrYUGF",
            "grant_type": "client_credentials",
            "scope": self.scopes,
        }

        response = requests.post(settings.DFC_KEYCLOAK_URL, data=payload)

        if response.status_code == 200:
            return response.json()["access_token"]

        raise KeycloakAuthenticationException(
            f"Failed to get access token: {response.text}"
        )


class KeycloakResourceServerAuthentication(BaseAuthentication):
    """
    For authenticating a client with an identity provider, for access to a resource on this server.
    """

    def get_valid_claims(self, encoded_token):
        """
        :return: validated claims
        :raises authlib.jose.JoseError: if token or claims are invalid
        """
        url = f"{os.getenv('KEYCLOAK_URL')}/realms/{os.getenv('KEYCLOAK_REALM')}/protocol/openid-connect/certs"
        jwks_data = requests.get(url).json()
        claims = authlib_jwt.decode(
            encoded_token,
            jwks_data,
            claims_options={
                "aud": {"essential": True, "value": "account"},
                "client_id": {"essential": True},
            },
        )
        claims.validate()
        return claims

    def authenticate(self, request):
        token = request.META.get("HTTP_AUTHORIZATION")
        if not token:
            raise AuthenticationFailed("No authentication provided")

        try:
            claims = self.get_valid_claims(token.split(" ")[1])
            request.platform_urlid = claims["client_id"]
        except JoseError:
            raise AuthenticationFailed("Invalid token")

        return None
