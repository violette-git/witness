# Transparency Giving App (witness)
---
## **Overview**
---
Churches and Non-Profit Orginizations have always been vulnerable to fraud, but the transition into the information age has pushed this crime into the sunlight quite often over the past decade.

Whether it be an Usher scraping off the top, The Bookkeeper issuing checks to fake companies, or The Pastor using your hard earned money on his new car. ***All the while that church goal is still unmet.*** 

This app aims to cut the fraud out before it begins and shine a light into your community, reinforcing a trust in the communities we serve.

---
## **Features**
---
*As a community member, I want to be able to make payments to, and view all payments made to my orginization.*

---
### Tasks:
- ihihini
- khvkiugc

### Additional Features

- iufyiuf
- khgcdiytdc
- igiytf
### Data Model
---
``````python
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

``````

---
*As a community member, I want to be able to receive payments from orginizations, community members, and view all payments made to my orginization.*

---
### Tasks:
- ihihini
- khvkiugc

### Additional Features

- iufyiuf
- khgcdiytdc
- igiytf
### Data Model
---
``````python
class Need(models.Model):

    title = models.CharField(max_length=50)

    cost = models.FloatField(validators=[MinValueValidator(min)])

    type = models.CharField(max_length=50, choices=TYPE, default='')

    date_created = models.DateTimeField(auto_now_add=True)

    date_edited = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:

        return f"Member needs {self.cost} for {self.title}."



``````
---
*As a community admin, I want to be able to create goals, refund payments, view number of memebers, and view all payments made to my orginization.*

---
### Tasks:
- ihihini
- khvkiugc


### Additional Features

- iufyiuf
- khgcdiytdc
- igiytf

---
### Data Model
---




