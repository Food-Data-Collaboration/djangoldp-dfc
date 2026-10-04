class ResourceAnnexationError(Exception):
    """
    A data server is forbidden from attempting to create or modify resources
    with a urlid from a domain external to them.

    This is to prevent them becoming de-facto data controller of an external resource.
    """
