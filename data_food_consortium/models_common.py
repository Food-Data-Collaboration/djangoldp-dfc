from djangoldp.models import Model


class AbstractPlatform(Model):
    class Meta:
        abstract = True


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
