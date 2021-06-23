from django.dispatch import receiver
from django.db.models.signals import pre_save, post_delete
from .models import Account
from .utils import delete_file


@receiver(pre_save, sender=Account)
def updateAccountHandler(sender, instance, **kwargs):
    try:
        old_img = Account.objects.get(pk=instance.pk).image_site
    except Account.DoesNotExist:
        return
    new_img = instance.image_site

    if old_img.url.split('/')[-1] != new_img.url.split('/')[-1] and old_img != 'images/default.png':
        delete_file(old_img.path)


@receiver(post_delete, sender=Account)
def deleteAccountHandler(sender, instance, **kwargs):
    image_file = instance.image_site
    if image_file != 'images/default.png':
        delete_file(image_file.path)
