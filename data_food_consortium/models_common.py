import urllib

from djangoldp.models import LDPModelManager, Model


class PlatformManager(LDPModelManager):
    def get(self, *args, **kwargs):
        # Avoid duplicate platform hosts with different paths.
        if "urlid" in kwargs:
            urlid = urllib.parse.urlparse(kwargs["urlid"])
            kwargs["urlid"] = f"{urlid.scheme}://{urlid.netloc}"
        return super().get(*args, **kwargs)


class AbstractPlatform(Model):
    objects = PlatformManager()

    class Meta:
        abstract = True
        rdf_type = "dfc-t:Platform"

    @classmethod
    def get_unique_kwargs(self, urlid):
        # Used to override some behaviour in the CSV import (see forms.py)
        return {"urlid": urlid}


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
