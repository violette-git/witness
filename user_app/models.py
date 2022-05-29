from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class User(AbstractUser):

    firstname = models.CharField(max_length=50)

    lastname = models.CharField(max_length=50)
    
    username = models.CharField(max_length=23, unique = True)

    user = models.IntegerField(null=True)

    email = models.EmailField(unique=True)

    password = models.CharField(max_length=250)

    profile_pic = models.ImageField()

    def __str__(self):

        return self.username