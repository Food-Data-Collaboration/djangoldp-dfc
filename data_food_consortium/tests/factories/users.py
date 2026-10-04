import factory
from django.conf import settings
from django.db.models.signals import post_save
from djangoldp.factories import UserFactory


@factory.django.mute_signals(post_save)
class DFCUserFactory(UserFactory):
    class Meta:
        model = settings.AUTH_USER_MODEL

    urlid = factory.Sequence(lambda n: "%s/users/%d" % (settings.SITE_URL, n))
    allow_create_backlink = False
