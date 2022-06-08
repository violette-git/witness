from django.db import models
from user_app.models import User
from django.core.validators import MinValueValidator
from tithe_app.models import Offering



class Organization(models.Model):

    business_name = models.CharField(max_length=70)

    website_url = models.URLField(max_length=200, blank=True, null=True)

    facebook_url = models.URLField(max_length=200, blank=True, null=True)

    mission_statement = models.CharField(max_length=1000, blank=True, null=True)
    
    members = models.ManyToManyField(User, related_name='member')

    offering = models.ForeignKey(Offering, on_delete=models.CASCADE, related_name='offerings')

    is_nonprofit = models.BooleanField(default=False, verbose_name='Non-Profit')


# ----------------------------------------------------------------------------------------------

class Goal(models.Model):

    title =  models.CharField(max_length=70)

    goal = models.FloatField(validators=[MinValueValidator(min)])

    description = models.CharField(max_length=1000)

    offering = models.ForeignKey(Offering, on_delete=models.CASCADE, related_name='goals')

    is_complete = models.BooleanField(default=False, verbose_name='goal reached')