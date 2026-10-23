from djangoldp_account.auth.backends import ExternalUserBackend


class KeycloakUserBackend(ExternalUserBackend):
    def unpack_bearer_jwt(self, token):
        self.id_token = super().unpack_bearer_jwt(token)

    def authenticate(self, request, username=None, password=None, **kwargs):
        if "authorization" in request.headers:
            jwt = request.headers["authorization"]

            if not jwt.lower().startswith("bearer"):
                return
            jwt = jwt[7:]

            user = self.validate_bearer_token(jwt)
            request.user_claims = self.id_token
            return user
