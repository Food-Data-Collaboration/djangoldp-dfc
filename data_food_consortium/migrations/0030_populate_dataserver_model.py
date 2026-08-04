from django.db import migrations

# We don't get these programatically because new models may have been created in the interim.
DFC_MODELS_AT_MIGRATION_TIME = [
    "Person",
    "CustomerCategory",
    "SocialMedia",
    "LocalizedProduct",
    "CatalogItem",
    "Price",
    "Offer",
    "Service",
    "EnterpriseService",
    "PhysicalPlace",
    "Coordination",
    "PhysicalPlaceAddress",
    "Enterprise",
    "SuppliedProduct",
    "SuppliedProductGroup",
    "EnterpriseAddress",
    "ShippingOption",
    "SaleSession",
]


def populate_dataserver_models(apps, schema_editor):
    """Populate DataServer model from the distinct values of data_server_source across all DFC models"""

    DataServer = apps.get_model("data_food_consortium", "DataServer")
    data_server_set = set()
    for model_name in DFC_MODELS_AT_MIGRATION_TIME:
        model = apps.get_model("data_food_consortium", model_name)
        data_server_set = data_server_set.union(
            set(model.objects.values_list("data_server_source", flat=True).distinct())
        )
    data_servers = [DataServer(urlid=d) for d in data_server_set]
    DataServer.objects.bulk_create(data_servers)


def depopulate_dataserver_models(apps, schema_editor):
    DataServer = apps.get_model("data_food_consortium", "DataServer")
    DataServer.objects.all().delete()


def set_dataserver_fks(apps, schema_editor):
    """Sets the dataserver_soirce_new foreign key fields for all DFC tables."""

    DataServer = apps.get_model("data_food_consortium", "DataServer")
    # Acceptable performance, few DataServer rows.
    data_server_lookup = {d.urlid: d.id for d in DataServer.objects.all()}

    for model_name in DFC_MODELS_AT_MIGRATION_TIME:
        model = apps.get_model("data_food_consortium", model_name)
        updated_rows = model.objects.all()
        for row in updated_rows:
            row.data_server_source_new_id = data_server_lookup[row.data_server_source]
        model.objects.bulk_update(updated_rows, ["data_server_source_new_id"])


def unset_dataserver_fks(apps, schema_editor):
    # Needs to be unset before DataServer instances can be deleted.
    for model_name in DFC_MODELS_AT_MIGRATION_TIME:
        model = apps.get_model("data_food_consortium", model_name)
        model.objects.all().update(data_server_source_new=None)


class Migration(migrations.Migration):
    dependencies = [("data_food_consortium", "0029_create_dataserver_model")]

    operations = [
        migrations.RunPython(
            populate_dataserver_models, reverse_code=depopulate_dataserver_models
        ),
        migrations.RunPython(set_dataserver_fks, reverse_code=unset_dataserver_fks),
        migrations.RemoveField(
            model_name="catalogitem",
            name="data_server_source",
        ),
        migrations.RemoveField(
            model_name="coordination",
            name="data_server_source",
        ),
        migrations.RemoveField(
            model_name="customercategory",
            name="data_server_source",
        ),
        migrations.RemoveField(
            model_name="enterprise",
            name="data_server_source",
        ),
        migrations.RemoveField(
            model_name="enterpriseaddress",
            name="data_server_source",
        ),
        migrations.RemoveField(
            model_name="enterpriseservice",
            name="data_server_source",
        ),
        migrations.RemoveField(
            model_name="localizedproduct",
            name="data_server_source",
        ),
        migrations.RemoveField(
            model_name="offer",
            name="data_server_source",
        ),
        migrations.RemoveField(
            model_name="person",
            name="data_server_source",
        ),
        migrations.RemoveField(
            model_name="physicalplace",
            name="data_server_source",
        ),
        migrations.RemoveField(
            model_name="physicalplaceaddress",
            name="data_server_source",
        ),
        migrations.RemoveField(
            model_name="price",
            name="data_server_source",
        ),
        migrations.RemoveField(
            model_name="salesession",
            name="data_server_source",
        ),
        migrations.RemoveField(
            model_name="service",
            name="data_server_source",
        ),
        migrations.RemoveField(
            model_name="shippingoption",
            name="data_server_source",
        ),
        migrations.RemoveField(
            model_name="socialmedia",
            name="data_server_source",
        ),
        migrations.RemoveField(
            model_name="suppliedproduct",
            name="data_server_source",
        ),
        migrations.RenameField(
            model_name="catalogitem",
            old_name="data_server_source_new",
            new_name="data_server_source",
        ),
        migrations.RenameField(
            model_name="coordination",
            old_name="data_server_source_new",
            new_name="data_server_source",
        ),
        migrations.RenameField(
            model_name="customercategory",
            old_name="data_server_source_new",
            new_name="data_server_source",
        ),
        migrations.RenameField(
            model_name="enterprise",
            old_name="data_server_source_new",
            new_name="data_server_source",
        ),
        migrations.RenameField(
            model_name="enterpriseaddress",
            old_name="data_server_source_new",
            new_name="data_server_source",
        ),
        migrations.RenameField(
            model_name="enterpriseservice",
            old_name="data_server_source_new",
            new_name="data_server_source",
        ),
        migrations.RenameField(
            model_name="localizedproduct",
            old_name="data_server_source_new",
            new_name="data_server_source",
        ),
        migrations.RenameField(
            model_name="offer",
            old_name="data_server_source_new",
            new_name="data_server_source",
        ),
        migrations.RenameField(
            model_name="person",
            old_name="data_server_source_new",
            new_name="data_server_source",
        ),
        migrations.RenameField(
            model_name="physicalplace",
            old_name="data_server_source_new",
            new_name="data_server_source",
        ),
        migrations.RenameField(
            model_name="physicalplaceaddress",
            old_name="data_server_source_new",
            new_name="data_server_source",
        ),
        migrations.RenameField(
            model_name="price",
            old_name="data_server_source_new",
            new_name="data_server_source",
        ),
        migrations.RenameField(
            model_name="salesession",
            old_name="data_server_source_new",
            new_name="data_server_source",
        ),
        migrations.RenameField(
            model_name="service",
            old_name="data_server_source_new",
            new_name="data_server_source",
        ),
        migrations.RenameField(
            model_name="shippingoption",
            old_name="data_server_source_new",
            new_name="data_server_source",
        ),
        migrations.RenameField(
            model_name="socialmedia",
            old_name="data_server_source_new",
            new_name="data_server_source",
        ),
        migrations.RenameField(
            model_name="suppliedproduct",
            old_name="data_server_source_new",
            new_name="data_server_source",
        ),
    ]
