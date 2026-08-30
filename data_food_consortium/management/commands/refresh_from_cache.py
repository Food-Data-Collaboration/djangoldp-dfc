from django.core.management.base import BaseCommand

from data_food_consortium.enums import ResourceImportSource
from data_food_consortium.models_common import DataServer
from data_food_consortium.proxy.resource import ResourceServerClient


class Command(BaseCommand):
    help = "Django command for updating the DFC models database from source"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        for data_server in DataServer.objects.all():
            ResourceServerClient(data_server.urlid).request_all_scopes(
                ResourceImportSource.COMMAND_LINE
            )
