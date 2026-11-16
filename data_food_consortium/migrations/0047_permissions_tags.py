import django_tagulous.models.fields
import django_tagulous.models.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "data_food_consortium",
            "0046_grantpolicy_dataservergrantpolicy_grantrequirement",
        ),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="suppliedproductgroup",
            options={},
        ),
        migrations.CreateModel(
            name="Tagulous_AbstractAddress_perms_tags",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("slug", models.SlugField()),
                (
                    "count",
                    models.IntegerField(
                        default=0,
                        help_text="Internal counter of how many times this tag is in use",
                    ),
                ),
                (
                    "protected",
                    models.BooleanField(
                        default=False,
                        help_text="Will not be deleted when the count reaches 0",
                    ),
                ),
            ],
            options={
                "ordering": ("name",),
                "abstract": False,
                "unique_together": {("slug",)},
            },
            bases=(django_tagulous.models.models.BaseTagModel, models.Model),
        ),
        migrations.CreateModel(
            name="Tagulous_AbstractAgent_perms_tags",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("slug", models.SlugField()),
                (
                    "count",
                    models.IntegerField(
                        default=0,
                        help_text="Internal counter of how many times this tag is in use",
                    ),
                ),
                (
                    "protected",
                    models.BooleanField(
                        default=False,
                        help_text="Will not be deleted when the count reaches 0",
                    ),
                ),
            ],
            options={
                "ordering": ("name",),
                "abstract": False,
                "unique_together": {("slug",)},
            },
            bases=(django_tagulous.models.models.BaseTagModel, models.Model),
        ),
        migrations.CreateModel(
            name="Tagulous_AbstractDFCModel_perms_tags",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("slug", models.SlugField()),
                (
                    "count",
                    models.IntegerField(
                        default=0,
                        help_text="Internal counter of how many times this tag is in use",
                    ),
                ),
                (
                    "protected",
                    models.BooleanField(
                        default=False,
                        help_text="Will not be deleted when the count reaches 0",
                    ),
                ),
            ],
            options={
                "ordering": ("name",),
                "abstract": False,
                "unique_together": {("slug",)},
            },
            bases=(django_tagulous.models.models.BaseTagModel, models.Model),
        ),
        migrations.CreateModel(
            name="Tagulous_AbstractProduct_perms_tags",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("slug", models.SlugField()),
                (
                    "count",
                    models.IntegerField(
                        default=0,
                        help_text="Internal counter of how many times this tag is in use",
                    ),
                ),
                (
                    "protected",
                    models.BooleanField(
                        default=False,
                        help_text="Will not be deleted when the count reaches 0",
                    ),
                ),
            ],
            options={
                "ordering": ("name",),
                "abstract": False,
                "unique_together": {("slug",)},
            },
            bases=(django_tagulous.models.models.BaseTagModel, models.Model),
        ),
        migrations.CreateModel(
            name="Tagulous_CatalogItem_perms_tags",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("slug", models.SlugField()),
                (
                    "count",
                    models.IntegerField(
                        default=0,
                        help_text="Internal counter of how many times this tag is in use",
                    ),
                ),
                (
                    "protected",
                    models.BooleanField(
                        default=False,
                        help_text="Will not be deleted when the count reaches 0",
                    ),
                ),
            ],
            options={
                "ordering": ("name",),
                "abstract": False,
                "unique_together": {("slug",)},
            },
            bases=(django_tagulous.models.models.BaseTagModel, models.Model),
        ),
        migrations.AddField(
            model_name="catalogitem",
            name="perms_tags",
            field=django_tagulous.models.fields.TagField(
                _set_tag_meta=True,
                force_lowercase=True,
                help_text="Labels for data used in permissions",
                to="data_food_consortium.tagulous_catalogitem_perms_tags",
                verbose_name="Permissions tags",
            ),
        ),
        migrations.CreateModel(
            name="Tagulous_Certification_perms_tags",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("slug", models.SlugField()),
                (
                    "count",
                    models.IntegerField(
                        default=0,
                        help_text="Internal counter of how many times this tag is in use",
                    ),
                ),
                (
                    "protected",
                    models.BooleanField(
                        default=False,
                        help_text="Will not be deleted when the count reaches 0",
                    ),
                ),
            ],
            options={
                "ordering": ("name",),
                "abstract": False,
                "unique_together": {("slug",)},
            },
            bases=(django_tagulous.models.models.BaseTagModel, models.Model),
        ),
        migrations.AddField(
            model_name="certification",
            name="perms_tags",
            field=django_tagulous.models.fields.TagField(
                _set_tag_meta=True,
                force_lowercase=True,
                help_text="Labels for data used in permissions",
                to="data_food_consortium.tagulous_certification_perms_tags",
                verbose_name="Permissions tags",
            ),
        ),
        migrations.CreateModel(
            name="Tagulous_Coordination_perms_tags",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("slug", models.SlugField()),
                (
                    "count",
                    models.IntegerField(
                        default=0,
                        help_text="Internal counter of how many times this tag is in use",
                    ),
                ),
                (
                    "protected",
                    models.BooleanField(
                        default=False,
                        help_text="Will not be deleted when the count reaches 0",
                    ),
                ),
            ],
            options={
                "ordering": ("name",),
                "abstract": False,
                "unique_together": {("slug",)},
            },
            bases=(django_tagulous.models.models.BaseTagModel, models.Model),
        ),
        migrations.AddField(
            model_name="coordination",
            name="perms_tags",
            field=django_tagulous.models.fields.TagField(
                _set_tag_meta=True,
                force_lowercase=True,
                help_text="Labels for data used in permissions",
                to="data_food_consortium.tagulous_coordination_perms_tags",
                verbose_name="Permissions tags",
            ),
        ),
        migrations.CreateModel(
            name="Tagulous_CustomerCategory_perms_tags",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("slug", models.SlugField()),
                (
                    "count",
                    models.IntegerField(
                        default=0,
                        help_text="Internal counter of how many times this tag is in use",
                    ),
                ),
                (
                    "protected",
                    models.BooleanField(
                        default=False,
                        help_text="Will not be deleted when the count reaches 0",
                    ),
                ),
            ],
            options={
                "ordering": ("name",),
                "abstract": False,
                "unique_together": {("slug",)},
            },
            bases=(django_tagulous.models.models.BaseTagModel, models.Model),
        ),
        migrations.AddField(
            model_name="customercategory",
            name="perms_tags",
            field=django_tagulous.models.fields.TagField(
                _set_tag_meta=True,
                force_lowercase=True,
                help_text="Labels for data used in permissions",
                to="data_food_consortium.tagulous_customercategory_perms_tags",
                verbose_name="Permissions tags",
            ),
        ),
        migrations.CreateModel(
            name="Tagulous_LocalizedProduct_perms_tags",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("slug", models.SlugField()),
                (
                    "count",
                    models.IntegerField(
                        default=0,
                        help_text="Internal counter of how many times this tag is in use",
                    ),
                ),
                (
                    "protected",
                    models.BooleanField(
                        default=False,
                        help_text="Will not be deleted when the count reaches 0",
                    ),
                ),
            ],
            options={
                "ordering": ("name",),
                "abstract": False,
                "unique_together": {("slug",)},
            },
            bases=(django_tagulous.models.models.BaseTagModel, models.Model),
        ),
        migrations.AddField(
            model_name="localizedproduct",
            name="perms_tags",
            field=django_tagulous.models.fields.TagField(
                _set_tag_meta=True,
                force_lowercase=True,
                help_text="Labels for data used in permissions",
                to="data_food_consortium.tagulous_localizedproduct_perms_tags",
                verbose_name="Permissions tags",
            ),
        ),
        migrations.CreateModel(
            name="Tagulous_Offer_perms_tags",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("slug", models.SlugField()),
                (
                    "count",
                    models.IntegerField(
                        default=0,
                        help_text="Internal counter of how many times this tag is in use",
                    ),
                ),
                (
                    "protected",
                    models.BooleanField(
                        default=False,
                        help_text="Will not be deleted when the count reaches 0",
                    ),
                ),
            ],
            options={
                "ordering": ("name",),
                "abstract": False,
                "unique_together": {("slug",)},
            },
            bases=(django_tagulous.models.models.BaseTagModel, models.Model),
        ),
        migrations.AddField(
            model_name="offer",
            name="perms_tags",
            field=django_tagulous.models.fields.TagField(
                _set_tag_meta=True,
                force_lowercase=True,
                help_text="Labels for data used in permissions",
                to="data_food_consortium.tagulous_offer_perms_tags",
                verbose_name="Permissions tags",
            ),
        ),
        migrations.CreateModel(
            name="Tagulous_Organization_perms_tags",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("slug", models.SlugField()),
                (
                    "count",
                    models.IntegerField(
                        default=0,
                        help_text="Internal counter of how many times this tag is in use",
                    ),
                ),
                (
                    "protected",
                    models.BooleanField(
                        default=False,
                        help_text="Will not be deleted when the count reaches 0",
                    ),
                ),
            ],
            options={
                "ordering": ("name",),
                "abstract": False,
                "unique_together": {("slug",)},
            },
            bases=(django_tagulous.models.models.BaseTagModel, models.Model),
        ),
        migrations.AddField(
            model_name="organization",
            name="perms_tags",
            field=django_tagulous.models.fields.TagField(
                _set_tag_meta=True,
                force_lowercase=True,
                help_text="Labels for data used in permissions",
                to="data_food_consortium.tagulous_organization_perms_tags",
                verbose_name="Permissions tags",
            ),
        ),
        migrations.CreateModel(
            name="Tagulous_OrganizationAddress_perms_tags",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("slug", models.SlugField()),
                (
                    "count",
                    models.IntegerField(
                        default=0,
                        help_text="Internal counter of how many times this tag is in use",
                    ),
                ),
                (
                    "protected",
                    models.BooleanField(
                        default=False,
                        help_text="Will not be deleted when the count reaches 0",
                    ),
                ),
            ],
            options={
                "ordering": ("name",),
                "abstract": False,
                "unique_together": {("slug",)},
            },
            bases=(django_tagulous.models.models.BaseTagModel, models.Model),
        ),
        migrations.AddField(
            model_name="organizationaddress",
            name="perms_tags",
            field=django_tagulous.models.fields.TagField(
                _set_tag_meta=True,
                force_lowercase=True,
                help_text="Labels for data used in permissions",
                to="data_food_consortium.tagulous_organizationaddress_perms_tags",
                verbose_name="Permissions tags",
            ),
        ),
        migrations.CreateModel(
            name="Tagulous_OrganizationService_perms_tags",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("slug", models.SlugField()),
                (
                    "count",
                    models.IntegerField(
                        default=0,
                        help_text="Internal counter of how many times this tag is in use",
                    ),
                ),
                (
                    "protected",
                    models.BooleanField(
                        default=False,
                        help_text="Will not be deleted when the count reaches 0",
                    ),
                ),
            ],
            options={
                "ordering": ("name",),
                "abstract": False,
                "unique_together": {("slug",)},
            },
            bases=(django_tagulous.models.models.BaseTagModel, models.Model),
        ),
        migrations.AddField(
            model_name="organizationservice",
            name="perms_tags",
            field=django_tagulous.models.fields.TagField(
                _set_tag_meta=True,
                force_lowercase=True,
                help_text="Labels for data used in permissions",
                to="data_food_consortium.tagulous_organizationservice_perms_tags",
                verbose_name="Permissions tags",
            ),
        ),
        migrations.CreateModel(
            name="Tagulous_Person_perms_tags",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("slug", models.SlugField()),
                (
                    "count",
                    models.IntegerField(
                        default=0,
                        help_text="Internal counter of how many times this tag is in use",
                    ),
                ),
                (
                    "protected",
                    models.BooleanField(
                        default=False,
                        help_text="Will not be deleted when the count reaches 0",
                    ),
                ),
            ],
            options={
                "ordering": ("name",),
                "abstract": False,
                "unique_together": {("slug",)},
            },
            bases=(django_tagulous.models.models.BaseTagModel, models.Model),
        ),
        migrations.AddField(
            model_name="person",
            name="perms_tags",
            field=django_tagulous.models.fields.TagField(
                _set_tag_meta=True,
                force_lowercase=True,
                help_text="Labels for data used in permissions",
                to="data_food_consortium.tagulous_person_perms_tags",
                verbose_name="Permissions tags",
            ),
        ),
        migrations.CreateModel(
            name="Tagulous_PhysicalPlace_perms_tags",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("slug", models.SlugField()),
                (
                    "count",
                    models.IntegerField(
                        default=0,
                        help_text="Internal counter of how many times this tag is in use",
                    ),
                ),
                (
                    "protected",
                    models.BooleanField(
                        default=False,
                        help_text="Will not be deleted when the count reaches 0",
                    ),
                ),
            ],
            options={
                "ordering": ("name",),
                "abstract": False,
                "unique_together": {("slug",)},
            },
            bases=(django_tagulous.models.models.BaseTagModel, models.Model),
        ),
        migrations.AddField(
            model_name="physicalplace",
            name="perms_tags",
            field=django_tagulous.models.fields.TagField(
                _set_tag_meta=True,
                force_lowercase=True,
                help_text="Labels for data used in permissions",
                to="data_food_consortium.tagulous_physicalplace_perms_tags",
                verbose_name="Permissions tags",
            ),
        ),
        migrations.CreateModel(
            name="Tagulous_PhysicalPlaceAddress_perms_tags",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("slug", models.SlugField()),
                (
                    "count",
                    models.IntegerField(
                        default=0,
                        help_text="Internal counter of how many times this tag is in use",
                    ),
                ),
                (
                    "protected",
                    models.BooleanField(
                        default=False,
                        help_text="Will not be deleted when the count reaches 0",
                    ),
                ),
            ],
            options={
                "ordering": ("name",),
                "abstract": False,
                "unique_together": {("slug",)},
            },
            bases=(django_tagulous.models.models.BaseTagModel, models.Model),
        ),
        migrations.AddField(
            model_name="physicalplaceaddress",
            name="perms_tags",
            field=django_tagulous.models.fields.TagField(
                _set_tag_meta=True,
                force_lowercase=True,
                help_text="Labels for data used in permissions",
                to="data_food_consortium.tagulous_physicalplaceaddress_perms_tags",
                verbose_name="Permissions tags",
            ),
        ),
        migrations.CreateModel(
            name="Tagulous_Price_perms_tags",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("slug", models.SlugField()),
                (
                    "count",
                    models.IntegerField(
                        default=0,
                        help_text="Internal counter of how many times this tag is in use",
                    ),
                ),
                (
                    "protected",
                    models.BooleanField(
                        default=False,
                        help_text="Will not be deleted when the count reaches 0",
                    ),
                ),
            ],
            options={
                "ordering": ("name",),
                "abstract": False,
                "unique_together": {("slug",)},
            },
            bases=(django_tagulous.models.models.BaseTagModel, models.Model),
        ),
        migrations.AddField(
            model_name="price",
            name="perms_tags",
            field=django_tagulous.models.fields.TagField(
                _set_tag_meta=True,
                force_lowercase=True,
                help_text="Labels for data used in permissions",
                to="data_food_consortium.tagulous_price_perms_tags",
                verbose_name="Permissions tags",
            ),
        ),
        migrations.CreateModel(
            name="Tagulous_SaleSession_perms_tags",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("slug", models.SlugField()),
                (
                    "count",
                    models.IntegerField(
                        default=0,
                        help_text="Internal counter of how many times this tag is in use",
                    ),
                ),
                (
                    "protected",
                    models.BooleanField(
                        default=False,
                        help_text="Will not be deleted when the count reaches 0",
                    ),
                ),
            ],
            options={
                "ordering": ("name",),
                "abstract": False,
                "unique_together": {("slug",)},
            },
            bases=(django_tagulous.models.models.BaseTagModel, models.Model),
        ),
        migrations.AddField(
            model_name="salesession",
            name="perms_tags",
            field=django_tagulous.models.fields.TagField(
                _set_tag_meta=True,
                force_lowercase=True,
                help_text="Labels for data used in permissions",
                to="data_food_consortium.tagulous_salesession_perms_tags",
                verbose_name="Permissions tags",
            ),
        ),
        migrations.CreateModel(
            name="Tagulous_Service_perms_tags",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("slug", models.SlugField()),
                (
                    "count",
                    models.IntegerField(
                        default=0,
                        help_text="Internal counter of how many times this tag is in use",
                    ),
                ),
                (
                    "protected",
                    models.BooleanField(
                        default=False,
                        help_text="Will not be deleted when the count reaches 0",
                    ),
                ),
            ],
            options={
                "ordering": ("name",),
                "abstract": False,
                "unique_together": {("slug",)},
            },
            bases=(django_tagulous.models.models.BaseTagModel, models.Model),
        ),
        migrations.AddField(
            model_name="service",
            name="perms_tags",
            field=django_tagulous.models.fields.TagField(
                _set_tag_meta=True,
                force_lowercase=True,
                help_text="Labels for data used in permissions",
                to="data_food_consortium.tagulous_service_perms_tags",
                verbose_name="Permissions tags",
            ),
        ),
        migrations.CreateModel(
            name="Tagulous_ShippingOption_perms_tags",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("slug", models.SlugField()),
                (
                    "count",
                    models.IntegerField(
                        default=0,
                        help_text="Internal counter of how many times this tag is in use",
                    ),
                ),
                (
                    "protected",
                    models.BooleanField(
                        default=False,
                        help_text="Will not be deleted when the count reaches 0",
                    ),
                ),
            ],
            options={
                "ordering": ("name",),
                "abstract": False,
                "unique_together": {("slug",)},
            },
            bases=(django_tagulous.models.models.BaseTagModel, models.Model),
        ),
        migrations.AddField(
            model_name="shippingoption",
            name="perms_tags",
            field=django_tagulous.models.fields.TagField(
                _set_tag_meta=True,
                force_lowercase=True,
                help_text="Labels for data used in permissions",
                to="data_food_consortium.tagulous_shippingoption_perms_tags",
                verbose_name="Permissions tags",
            ),
        ),
        migrations.CreateModel(
            name="Tagulous_SocialMedia_perms_tags",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("slug", models.SlugField()),
                (
                    "count",
                    models.IntegerField(
                        default=0,
                        help_text="Internal counter of how many times this tag is in use",
                    ),
                ),
                (
                    "protected",
                    models.BooleanField(
                        default=False,
                        help_text="Will not be deleted when the count reaches 0",
                    ),
                ),
            ],
            options={
                "ordering": ("name",),
                "abstract": False,
                "unique_together": {("slug",)},
            },
            bases=(django_tagulous.models.models.BaseTagModel, models.Model),
        ),
        migrations.AddField(
            model_name="socialmedia",
            name="perms_tags",
            field=django_tagulous.models.fields.TagField(
                _set_tag_meta=True,
                force_lowercase=True,
                help_text="Labels for data used in permissions",
                to="data_food_consortium.tagulous_socialmedia_perms_tags",
                verbose_name="Permissions tags",
            ),
        ),
        migrations.CreateModel(
            name="Tagulous_SuppliedProduct_perms_tags",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("slug", models.SlugField()),
                (
                    "count",
                    models.IntegerField(
                        default=0,
                        help_text="Internal counter of how many times this tag is in use",
                    ),
                ),
                (
                    "protected",
                    models.BooleanField(
                        default=False,
                        help_text="Will not be deleted when the count reaches 0",
                    ),
                ),
            ],
            options={
                "ordering": ("name",),
                "abstract": False,
                "unique_together": {("slug",)},
            },
            bases=(django_tagulous.models.models.BaseTagModel, models.Model),
        ),
        migrations.AddField(
            model_name="suppliedproduct",
            name="perms_tags",
            field=django_tagulous.models.fields.TagField(
                _set_tag_meta=True,
                force_lowercase=True,
                help_text="Labels for data used in permissions",
                to="data_food_consortium.tagulous_suppliedproduct_perms_tags",
                verbose_name="Permissions tags",
            ),
        ),
        migrations.CreateModel(
            name="Tagulous_TemplateSaleSession_perms_tags",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("slug", models.SlugField()),
                (
                    "count",
                    models.IntegerField(
                        default=0,
                        help_text="Internal counter of how many times this tag is in use",
                    ),
                ),
                (
                    "protected",
                    models.BooleanField(
                        default=False,
                        help_text="Will not be deleted when the count reaches 0",
                    ),
                ),
            ],
            options={
                "ordering": ("name",),
                "abstract": False,
                "unique_together": {("slug",)},
            },
            bases=(django_tagulous.models.models.BaseTagModel, models.Model),
        ),
        migrations.AddField(
            model_name="templatesalesession",
            name="perms_tags",
            field=django_tagulous.models.fields.TagField(
                _set_tag_meta=True,
                force_lowercase=True,
                help_text="Labels for data used in permissions",
                to="data_food_consortium.tagulous_templatesalesession_perms_tags",
                verbose_name="Permissions tags",
            ),
        ),
        migrations.CreateModel(
            name="Tagulous_Vevent_perms_tags",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("slug", models.SlugField()),
                (
                    "count",
                    models.IntegerField(
                        default=0,
                        help_text="Internal counter of how many times this tag is in use",
                    ),
                ),
                (
                    "protected",
                    models.BooleanField(
                        default=False,
                        help_text="Will not be deleted when the count reaches 0",
                    ),
                ),
            ],
            options={
                "ordering": ("name",),
                "abstract": False,
                "unique_together": {("slug",)},
            },
            bases=(django_tagulous.models.models.BaseTagModel, models.Model),
        ),
        migrations.AddField(
            model_name="vevent",
            name="perms_tags",
            field=django_tagulous.models.fields.TagField(
                _set_tag_meta=True,
                force_lowercase=True,
                help_text="Labels for data used in permissions",
                to="data_food_consortium.tagulous_vevent_perms_tags",
                verbose_name="Permissions tags",
            ),
        ),
    ]
