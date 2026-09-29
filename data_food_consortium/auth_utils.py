from urllib.parse import urlparse

from data_food_consortium.enums import PermissioningScope


def get_required_scope_for_model(model):
    return getattr(model._meta, "dfc_read_scope", PermissioningScope.READ_ENTERPRISE)


def user_oidc_provider(user):
    # NOTE: assumption made that the OIDC provider of the user is connected to their urlid
    parsed_urlid = urlparse(user.urlid)
    return f"{parsed_urlid.scheme}://{parsed_urlid.netloc}/"
