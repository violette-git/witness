# Transparency Giving App (witness)
---
## **Overview**
---
Churches and Non-Profit Orginizations have always been vulnerable to fraud, but the transition into the information age has pushed this crime into the sunlight quite often over the past decade.

Whether it be an Usher scraping off the top, The Bookkeeper issuing checks to fake companies, or The Pastor using your hard earned money on his new car. ***All the while, that church goal is still unmet.*** 

This app aims to cut the fraud out before it begins and shine a light into your community, reinforcing a trust in the communities we serve.

---
## **Features**
---
*As a community member, I want to be able to make payments to, view all payments made to, and see all withdrawals made by my orginization.*

---
### Tasks:
- Create Django models for user.
- Create Django models for tithe.
- Create Django models for offering.
- Create a form for signup, tith, offering.
- Create a view with returned form data.
- Design profile view.
-

### Additional Features

- User Dashboard.
- Anonymize Usernames.
- Previously Visited.
- Paypal Integration.
- Stripe Integration.
- Crypto Integration.
- Javascript Interactivity.
- 
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
*As a community member, I want to be able to receive payments from orginizations, community members, withdraw funds on behalf of my orginization, and view all payments made to my orginization.*

---
### Tasks:
- Create a Django model for need.
- Create a form form for need.
- Create a view with returned data.
- 

### Additional Features

- Javascript Interactivity
- 
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
*As a community admin, I want to be able to create goals, refund payments, view number of members, and view all payments made to my orginization.*

---
### Tasks:
- Create register form for community admin.
-


### Additional Features

- Create admin user model.
- Upon return and verification of orginization, create admin account.
- Create admin dashboard.
-

---
### Data Model
---
``````python
print('data model here')
``````
## Schedule
---
### Week #1
---
-
### Week #2
---
-
### Week #3
---
-
### Week #4
---
-

## Must Haves
---
- Need Creation.
- Ability to join multiple orginizations.
- Ability to contribute to a need.
- Ability to see every payment and withdrawal.


## Should Haves
---
- User Dashboard.
- SwiperJs CDN.
- Mobile Friendly/Responsive.
## Can Haves
---
- Custom Admin Dashboard.
- Crypto Payment.
- Public Messages.
- Donate Page.

---
# Stretch Goal
---
- ReactNative Rebuild.
- Javascript Animation.
- Advertising / Customer Generation.
- Host with Netlify.






