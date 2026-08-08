from djangoldp.models import Model


class AbstractPlatform(Model):
    class Meta:
        abstract = True

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
