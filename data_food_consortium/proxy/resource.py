import requests

from django.conf import settings

from data_food_consortium.proxy.keycloak import (
    KeycloakAuthenticationException,
    KeycloakClient,
)


class ResourceServerClient:
    """
    Manages the proxy's connection to a data source, authenticated with Keycloak.
    """

    dataserver_url = ""

    def __init__(self, dataserver_url):
        self.dataserver_url = dataserver_url

    def request_all_scopes(self):
        for scope in settings.DFC_KEYCLOAK_READ_SCOPES:
            # TODO: make a log of failures
            try:
                self.request_scope(scope)
            except KeycloakAuthenticationException as e:
                msg = f"ERR authenticating dataserver {self.dataserver_url} with Keycloak, while requesting {scope}"
                print(msg)
                print(str(e))
            except requests.exceptions.RequestException as e:
                msg = f"ERR requesting a scope {scope} from dataserver {self.dataserver_url}"
                print(msg)
                print(str(e))

    def request_scope(self, scope: str):
        """
        Requests an access token from Keycloak for a given scope, and then requests from the dataserver the associated endpoint.

        :raises KeycloakAuthenticationException: if authentication with Keycloak is unsuccessful
        :raises RequestException: if dataserver request is unsuccessful
        """
        token = KeycloakClient(scope).get_access_token()

        # Each scope has an associated endpoint
        headers = {"Authorization": f"Bearer {token}"}
        endpoint = f"{self.dataserver_url}{settings.DFC_KEYCLOAK_READ_SCOPES[scope]}"
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()
        data = response.json()

        # TODO: import the returned data
        print("Successfully got data " + str(data))
