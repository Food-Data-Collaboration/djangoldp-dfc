from djangoldp.filters import SearchByQueryParamFilterBackend
from djangoldp.views.ldp_viewset import LDPViewSet


class EnterpriseViewset(LDPViewSet):
    filter_backends = [SearchByQueryParamFilterBackend]


class PersonViewset(LDPViewSet):
    filter_backends = [SearchByQueryParamFilterBackend]
