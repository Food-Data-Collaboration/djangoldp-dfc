from django.apps import AppConfig


class DataFoodConsortiumConfig(AppConfig):
    name = "data_food_consortium"

    def ready(self):
        from data_food_consortium import (
            models_common,
            models_permissioning,
        )
