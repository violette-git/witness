from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.



TYPE = (
    ('food', 'FOOD'),
    ('housing', 'HOUSING'),
    ('',''),

)

min = 0.00

class Need(models.Model):

    title = models.CharField(max_length=50)

    cost = models.FloatField(validators=[MinValueValidator(min)])

    type = models.CharField(max_length=50, choices=TYPE, default='')

    date_created = models.DateTimeField(auto_now_add=True)

    date_edited = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:

        return f"Member needs {self.cost} for {self.title}."

