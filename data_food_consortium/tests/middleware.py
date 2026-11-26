from django.conf import settings
from django.utils.deprecation import MiddlewareMixin


class InjectUserClaimsMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.user_claims = settings.TEST_USER_CLAIMS
