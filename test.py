
from django.db import models
from user_app.models import User
from django.core.validators import MinValueValidator
from django.contrib.auth.models import AbstractUser




class User(AbstractUser):
    
    username = models.CharField(max_length=23, unique = True)

    user = models.IntegerField(null=True)
    # choose between predetermined icons with
    # ability to change background color
    profile_pic = models.ImageField()

    is_superuser = models.BooleanField(default=False, verbose_name='admin status')

    def __str__(self):
    
        return self.username
        
# --------------------------------------------------------------------------------
min = 0.00

class Offering(models.Model):

    amount = models.FloatField(validators=[MinValueValidator(min)])

    date = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='offering')

    is_tithe = models.BooleanField(default=False, verbose_name='gift type')


    def __str__(self) -> str:

        if self.is_tithe == False:
        
            return f"Paid offering in the amount of {self.amount} on {self.date}."

        else:
            
            return f"Paid tiithes in the amount of {self.amount} on {self.date}."

# -----------------------------------------------------------------------------------------

class Orginization(models.Model):

    business_name = models.CharField(max_length=70)

    website_url = models.URLField(max_lenth=200, blank=True, null=True)

    facebook_url = models.URLField(max_lenth=200, blank=True, null=True)

    mission_statement = models.CharField(max_length=1000, blank=True, null=True)
    
    members = models.ManyToManyField(User, on_delete=models.CASCADE, related_name='member')

    offering = models.ForeignKey(Offering, related_name='offerings')

    is_nonprofit = models.BooleanField(default=False, verbose_name='org type')


# ----------------------------------------------------------------------------------------------

class Goal(models.Model):

    title =  models.CharField(max_length=70)

    goal = models.FloatField(validators=[MinValueValidator(min)])

    description = models.CharField(max_length=1000)

    offering = models.ForeignKey(Offering, related_name='goals')

<form class="d-flex" role="search">
                <input class="form-control me-2" type="search" placeholder="Search Organizations" aria-label="Search">
                <button class="btn btn-outline-success" type="submit">Search</button>
            </form>







