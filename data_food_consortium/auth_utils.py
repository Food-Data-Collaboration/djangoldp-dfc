from urllib.parse import urlparse

from data_food_consortium.enums import PermissioningScope


def get_required_scope_for_model(model):
    return getattr(model._meta, "dfc_read_scope", PermissioningScope.READ_ENTERPRISE)


def normalise_to_domain(urlid):
    parsed_urlid = urlparse(urlid)
    return f"{parsed_urlid.scheme}://{parsed_urlid.netloc}"


def user_oidc_provider(user):
    # NOTE: assumption made that the OIDC provider of the user is connected to their urlid
    return normalise_to_domain(user.urlid)


def resource_domain(urlid: str):
    return urlparse(urlid).netloc
