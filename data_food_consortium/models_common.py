import urllib

from djangoldp.models import Model


class AbstractPlatform(Model):
    class Meta:
        abstract = True
        rdf_type = "dfc-t:Platform"

    @classmethod
    def get_unique_kwargs(self, urlid):
        # Used to override some behaviour in the CSV import (see forms.py)
        return {"urlid": urlid}

    def save(self, *args, **kwargs):
        # Avoid duplicate platform hosts with different paths.
        urlid = urllib.parse.urlparse(self.urlid)
        self.urlid = f"{urlid.scheme}://{urlid.netloc}"
        return super().save(*args, **kwargs)


class DataServer(AbstractPlatform):
    """
    A data source, which granted a platform access to some data.
    """

    def __str__(self):
        return self.urlid


class Platform(AbstractPlatform):
    """
    A data consumer.
    """

    def __str__(self):
        return self.urlid
