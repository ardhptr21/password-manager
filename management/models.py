from django.db import models
from django.urls import reverse


class Account(models.Model):
    image_site = models.ImageField(
        upload_to="images", default="images/default.png", blank=True)
    site_name = models.URLField(max_length=255)
    email = models.EmailField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=False, blank=False)

    def get_absolute_url(self):
        return reverse('management:list')

    def __str__(self):
        return self.site_name
