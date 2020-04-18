from django.db.models.signals import post_save
from django.dispatch import receiver
import logging
from main.models import MyUser, Profile

logger = logging.getLogger('main')


@receiver(post_save, sender=MyUser)
def user_created(sender, instance, created, **kwargs):
    if created:
        logger.debug(f'user Profile crated for {instance}')
        logger.info(f'user Profile crated for {instance}')
        logger.warning(f'user Profile crated for {instance}')
        logger.error(f'user Profile crated for {instance}')
        logger.critical(f'user Profile crated for {instance}')
        Profile.objects.create(user=instance)
