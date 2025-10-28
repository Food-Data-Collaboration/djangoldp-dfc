from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class DisbaleJWTMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == reverse("djangoldp-dfc-webhook"):
            request.disable_jwt_middleware = True
