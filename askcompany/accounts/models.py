from django.db import models
from django.conf import settings
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
    adress = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=63) #,validators=[])