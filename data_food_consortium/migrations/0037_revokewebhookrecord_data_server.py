from urllib.parse import urlparse

import django.db.models.deletion
import djangoldp.fields
from django.db import migrations


def populate_webhook_record_data_servers(apps, schema_editor):
    """Populate DataServer model from the distinct values of data_server_source across all DFC models"""

    DataServer = apps.get_model("data_food_consortium", "DataServer")
    ResourceImportRecord = apps.get_model(
        "data_food_consortium", "ResourceImportRecord"
    )
    RevokeWebhookRecord = apps.get_model("data_food_consortium", "RevokeWebhookRecord")

    data_server_urlids = set(
        ResourceImportRecord.objects.values_list("data_server_source", flat=True)
    ).union(
        set(RevokeWebhookRecord.objects.values_list("data_server_urlid", flat=True))
    )
    dataserver_lookup_dict = {
        d: DataServer.objects.get_or_create(
            urlid=f"{urlparse(d).scheme}://{urlparse(d).netloc}"
        )[0]
        for d in data_server_urlids
    }

    updated_rows = ResourceImportRecord.objects.all()
    for row in updated_rows:
        row.data_server = dataserver_lookup_dict[row.data_server_source]
    ResourceImportRecord.objects.bulk_update(updated_rows, ["data_server"])

    updated_rows = RevokeWebhookRecord.objects.all()
    for row in updated_rows:
        row.data_server = dataserver_lookup_dict[row.data_server_urlid]
    RevokeWebhookRecord.objects.bulk_update(updated_rows, ["data_server"])

    ResourceImportRecord.objects.filter(data_server__isnull=True).delete()
    RevokeWebhookRecord.objects.filter(data_server__isnull=True).delete()


def set_str_data_server_values(apps, schema_editor):
    ResourceImportRecord = apps.get_model(
        "data_food_consortium", "ResourceImportRecord"
    )
    RevokeWebhookRecord = apps.get_model("data_food_consortium", "RevokeWebhookRecord")

    updated_rows = ResourceImportRecord.objects.all()
    for row in updated_rows:
        row.data_server_source = row.data_server.urlid
    ResourceImportRecord.objects.bulk_update(updated_rows, ["data_server_source"])

    updated_rows = RevokeWebhookRecord.objects.all()
    for row in updated_rows:
        row.data_server_urlid = row.data_server.urlid
    RevokeWebhookRecord.objects.bulk_update(updated_rows, ["data_server_urlid"])


class Migration(migrations.Migration):

    dependencies = [
        (
            "data_food_consortium",
            "0036_rename_platform_urlid_revokewebhookrecord_data_server_urlid",
        ),
    ]

    operations = [
        # Add Foreign Keys to Data Server on import records.
        migrations.AddField(
            model_name="resourceimportrecord",
            name="data_server",
            field=djangoldp.fields.ForeignKey(
                null=True,
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="data_food_consortium.dataserver",
            ),
        ),
        migrations.AddField(
            model_name="revokewebhookrecord",
            name="data_server",
            field=djangoldp.fields.ForeignKey(
                help_text="The data server which sent the webhook",
                null=True,
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="data_food_consortium.dataserver",
            ),
        ),
        # Script which ensures the DataServer field is set, and noncompliant records are removed.
        migrations.RunPython(
            populate_webhook_record_data_servers,
            reverse_code=set_str_data_server_values,
        ),
        # Make the fields not-null.
        migrations.AlterField(
            model_name="resourceimportrecord",
            name="data_server",
            field=djangoldp.fields.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="data_food_consortium.dataserver",
            ),
        ),
        migrations.AlterField(
            model_name="revokewebhookrecord",
            name="data_server",
            field=djangoldp.fields.ForeignKey(
                help_text="The data server which sent the webhook",
                on_delete=django.db.models.deletion.CASCADE,
                to="data_food_consortium.dataserver",
            ),
        ),
        # Remove the old data server fields from the records.
        migrations.RemoveField(
            model_name="resourceimportrecord",
            name="data_server_source",
        ),
        migrations.RemoveField(
            model_name="revokewebhookrecord",
            name="data_server_urlid",
        ),
    ]
