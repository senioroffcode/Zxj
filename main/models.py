from django.db import models
from django.contrib.auth.models import AbstractUser


class Region(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class User(AbstractUser):
    phone = models.CharField(max_length=244, null=True, blank=True)
    status = models.IntegerField(choices=(
        (1, 'director'),
        (2, 'call'),
        (3, 'kassir')
    ))
    region = models.ForeignKey(Region, on_delete=models.CASCADE)