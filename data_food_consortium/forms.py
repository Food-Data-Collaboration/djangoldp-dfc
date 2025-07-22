from djangoldp_csv.forms import BaseCSVImportForm, FileField
from data_food_consortium.models import Enterprise, EnterpriseAddress, SuppliedProduct


class EnterpriseImportForm(BaseCSVImportForm):
    """
    An extension of DjangoLDP-CSV's main form class designed to provide the import
    of all key data to an Enterprise in a single form.
    """

    supplied_products = FileField(model_type=SuppliedProduct)
    enterprises = FileField(model_type=Enterprise)
    addresses = FileField(model_type=EnterpriseAddress)
