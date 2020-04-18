from django.db.models.signals import post_save
from django.dispatch import receiver
import logging
from onlineShop.main.models import Category, CategoryFullInfo

logger = logging.getLogger('main')


@receiver(post_save, sender=Category)
def user_created(sender, instance, created, **kwargs):
    if created:
        logger.debug(f'CategoryFUllInfo crated for {instance}')
        logger.info(f'CategoryFUllInfo crated for {instance}')
        logger.warning(f'CategoryFUllInfo crated for {instance}')
        logger.error(f'CategoryFUllInfo crated for {instance}')
        logger.critical(f'CategoryFUllInfo crated for {instance}')
        CategoryFullInfo.objects.create(category=instance)
