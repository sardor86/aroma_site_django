from django.db import models


class Users(models.Model):
    email = models.CharField(max_length=100, unique=True, null=False)
    password = models.CharField(max_length=100, null=False)
