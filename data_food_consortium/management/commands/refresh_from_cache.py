from django.conf import settings
from django.core.management.base import BaseCommand

from data_food_consortium.proxy.resource import ResourceServerClient


class Command(BaseCommand):
    help = "Django command for updating the DFC models database from source"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        for dataserver_url in settings.DFC_DATASERVER_URLS:
            ResourceServerClient(dataserver_url).request_all_scopes()
