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
            self.request_scope(scope)

    def request_scope(self, scope: str):
        try:
            token = KeycloakClient(scope).get_access_token()
        except KeycloakAuthenticationException as e:
            # TODO: make a report of failures
            print(f"ERR while requesting {scope}")
            print(str(e))
            return

        # headers = {"Authorization": f"Bearer {token}"}
        print("got token " + str(token))
