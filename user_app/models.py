from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class User(AbstractUser):
    
    username = models.CharField(max_length=23, unique = True)

    user = models.IntegerField(null=True)
    # choose between predetermined icons with
    # ability to change background color
    profile_pic = models.ImageField()

    is_superuser = models.BooleanField(default=False, verbose_name='Admin Dashboard Access')

    def __str__(self):
    
        return self.username