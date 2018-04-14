import datetime
from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver

from mamba.models import Site


@receiver(post_save)
def signal_save_update(sender, instance, created, **kwargs):
    if isinstance(instance, Site):
        if created:
            pass
        else:
            pass


@receiver(post_delete)
def signal_delete(sender, instance, using, **kwargs):
    pass
