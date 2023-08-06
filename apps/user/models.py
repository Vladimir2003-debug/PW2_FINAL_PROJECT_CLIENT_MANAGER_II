from django.db import models
from django.urls import reverse
from apps.catalogo_cuentas.models import CatalogoCuentas,Country
from django.contrib.auth.models import User 
from apps.catalogo_cuentas.models import CatalogoCuentas,Country
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser

import uuid

# Create your models here.

GENDER_CHOICES = (
    ("M","Masculino"),
    ("F","Femenino"),
)

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return "user_{0}/{1}".format(instance.user.id, filename)

class User(AbstractUser):
    phone_number = models.IntegerField(default=0)
    country = models.CharField(max_length=100,default="Peru")
    address = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    birthday = models.DateField(auto_now=True)
    perfil_image = models.ImageField(default="", upload_to=user_directory_path)

    gender = models.TextField(choices=GENDER_CHOICES, default="M")
    is_admin = models.BooleanField("Is admin",default=False)
    is_cliente = models.BooleanField("Is cliente",default=False)
    is_contador = models.BooleanField("Is contador",default=False)
