from django.core.exceptions import ValidationError
from djangoldp_csv.forms import BaseCSVImportForm, FileField
from data_food_consortium.models import Enterprise, EnterpriseAddress, SuppliedProduct


class EnterpriseImportForm(BaseCSVImportForm):
    """
    An extension of DjangoLDP-CSV's main form class designed to provide the import
    of all key data to an Enterprise in a single form.
    """

    supplied_products = FileField(model_type=SuppliedProduct, required=False)
    enterprises = FileField(model_type=Enterprise, required=False)
    addresses = FileField(model_type=EnterpriseAddress, required=False)

    def clean(self):
        super().clean()

        # Assert that at least one file was uploaded.
        if not len(
            {self.cleaned_data[f.name] for f in self.file_fields()}.difference({None})
        ):
            raise ValidationError("Please upload at least one CSV file")
