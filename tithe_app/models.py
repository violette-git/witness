from django.db import models
from user_app.models import User
from django.core.validators import MinValueValidator



# Create your models here.
TYPE = (
    ('food', 'Food'),
    ('housing', 'Housing'),
    ('clothing', 'Clothing'),
    ('other','Other'),

)

min = 0.00
class Offering(models.Model):

    amount = models.FloatField(validators=[MinValueValidator(min)])

    date = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='offering')

    is_tithe = models.BooleanField(default=False, verbose_name='Tithe')

    def __str__(self) -> str:

        if self.is_tithe == False:
        
            return f"Paid offering in the amount of {self.amount} on {self.date}."

        else:
            
            return f"Paid tithes in the amount of {self.amount} on {self.date}."




class Need(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='needs', null=False, blank=False )

    title = models.CharField(max_length=50)

    cost = models.FloatField(validators=[MinValueValidator(min)])

    type = models.CharField(max_length=50, choices=TYPE, default='')

    date_created = models.DateTimeField(auto_now_add=True)

    date_edited = models.DateTimeField(auto_now=True)

    description = models.CharField(max_length=300, blank='False')

    # def field for percentage

    def __str__(self) -> str:

        return f"Member needs {self.cost} for {self.title}."