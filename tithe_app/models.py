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
class Need(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='needs', null=False, blank=False )

    title = models.CharField(max_length=50)

    cost = models.DecimalField(decimal_places=2, max_digits=10, validators=[MinValueValidator(min)])

    type = models.CharField(max_length=50, choices=TYPE, default='')

    date_created = models.DateTimeField(auto_now_add=True)

    date_edited = models.DateTimeField(auto_now=True)

    description = models.CharField(max_length=300, blank='False')
    
    goal_reached = models.BooleanField(default=False)

    donated_amount = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)

    def percentage_donated(self):

        return (self.donated_amount / self.cost ) * 100



    # def __str__(self) -> str:

    #     return f"Member needs {self.cost} for {self.title}."
class Offering(models.Model):

    amount = models.DecimalField(decimal_places=2, max_digits=10,null=False, validators=[MinValueValidator(min)])

    date = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='offering', null=True)

    is_tithe = models.BooleanField(default=False, verbose_name='Tithe',)

    need = models.ForeignKey(Need, on_delete=models.CASCADE, related_name='offerings')

    # def __str__(self) -> str:

    #     if self.is_tithe == False:
        
    #         return f"Paid offering in the amount of {self.amount} on {self.date}."

    #     else:
            
    #         return f"Paid tithes in the amount of {self.amount} on {self.date}."



