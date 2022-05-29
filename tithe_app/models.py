from django.db import models
from user_app.models import User
from django.core.validators import MinValueValidator



# Create your models here.

min = 0.00

class Tithe(models.Model):

    amount = models.FloatField(validators=[MinValueValidator(min)])

    date = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tithe')

    def __str__(self) -> str:

        return f"Paid tithes in the amount of {self.amount} on {self.date}."


class Offering(models.Model):

    amount = models.FloatField(validators=[MinValueValidator(min)])

    date = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='offering')

    def __str__(self) -> str:

        return f"Paid offering in the amount of {self.amount} on {self.date}."
