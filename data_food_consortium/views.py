from django.shortcuts import render
from djangoldp.filters import SearchByQueryParamFilterBackend
from djangoldp.views.ldp_viewset import LDPViewSet
from djangoldp_csv.errors import FieldParsingError
from djangoldp_csv.views import BaseCSVImportView
from data_food_consortium.forms import EnterpriseImportForm


class EnterpriseViewset(LDPViewSet):
    filter_backends = [SearchByQueryParamFilterBackend]


class PersonViewset(LDPViewSet):
    filter_backends = [SearchByQueryParamFilterBackend]


class EnterpriseImportView(BaseCSVImportView):
    def get_form_class(self, *args, **kwargs):
        return EnterpriseImportForm(*args, **kwargs)

    def render_import(self, request, form, success=False):
        return render(
            request, "enterprise_import.html", {"form": form, "success": success}
        )

    def get(self, request, *args, **kwargs):
        return self.render_import(request, self.get_form_class())

    def post(self, request, *args, **kwargs):
        form = self.get_form_class(request.POST, request.FILES)
        if not form.is_valid():
            return self.render_import(request, form)

        try:
            self.process_form(form)
        except FieldParsingError:
            return self.render_import(request, form)

        return self.render_import(request, form, success=True)
