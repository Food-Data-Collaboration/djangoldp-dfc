import os

import requests
from authlib.jose import jwt as authlib_jwt
from authlib.jose.errors import JoseError
from django.conf import settings
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from data_food_consortium.models_common import Platform


def keycloak_is_configured():
    """Returns True if keycloak settings have been configured on the server."""
    return None not in [
        settings.KEYCLOAK_URL,
        settings.KEYCLOAK_CLIENT_ID,
        settings.KEYCLOAK_CLIENT_SECRET,
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
            "client_id": settings.KEYCLOAK_CLIENT_ID,
            "client_secret": settings.KEYCLOAK_CLIENT_SECRET,
            "grant_type": "client_credentials",
            "scope": self.scopes,
        }

        response = requests.post(settings.KEYCLOAK_URL, data=payload)

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
            platform_urlid = claims["client_id"]
        except JoseError:
            raise AuthenticationFailed("Invalid token")
        except KeyError:
            raise AuthenticationFailed("Missing claim, client_id")

        try:
            request.platform = Platform.objects.get(urlid=platform_urlid)
        except Platform.DoesNotExist:
            # TODO: allow for different failure strategies: admin notification and open registration.
            # Allowing open registration here would only award the user access to public resources.
            raise AuthenticationFailed(
                f"Platform {platform_urlid} is not federated with this server"
            )
