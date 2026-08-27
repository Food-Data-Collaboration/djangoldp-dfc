from django.db.models import options

__version__ = "0.0.0"

options.DEFAULT_NAMES += ("dfc_read_scope", "dfc_write_scope")
