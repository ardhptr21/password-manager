from django.db import models


class Account(models.Model):
    site_name = models.URLField(max_length=255)
    email = models.EmailField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=False, blank=False)