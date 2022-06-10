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
## Data Model
---

</br>

### ***User***
---
|Variable|Field Type|Properties|
|--------|---------|---------|
|username|CharField|max_length=23,unique=True|
|user    |IntegerField|null=True|
|profile_pic|ImageField|    |
|is_superuser|BooleanField|default=False|

---
</br>

### ***Need***
---

|Variable|Field Type|Properties|
|--------|---------|---------|
|title|CharField|max_length=50|
|cost|FloatField|min=1.00|
|type|CharField|max_length=50, choices=TYPE, default=''|
|date_created|BooleanField|auto_now_add=True|
|date_edited|BooleanFieldauto_now=True|
</br>
### ***Offering***
---

|Variable|Field Type|Properties|
|--------|---------|---------|
|amount|FloatField|min=1.00|
|date   |DateTimeField|auto_now_add=True|
|user|ForeignKey|to User, related name = tithe    |
|is_tithe|BooleanField|default=False|
</br>


### ***Orginization***
---

|Variable|Field Type|Properties|
|--------|---------|---------|
|business_name|CharField|max_length=70|
|website_url|URLField|max_length=200|
|facebook_url|URLField|max_length=200|
|mission_statement|CharField|max_length=1000|
|members|ManyToManyField|User, related name=member|
|offering|ForeignKey|to Offering, related name=offerings|
|is_nonprofit|BooleanField|to User, related name = tithe|
</br>

### ***Goal***
---

|Variable|Field Type|Properties|
|--------|---------|---------|
|title|CharField|max_length=70|
|goal|FloatField|min=1.00|
|description|charField|max_length=1000|
|offering|ForeignKey|to Offering, related name=goals|
---

</br>

## **Schedule**
---
### Week #1
---
- Create Repo.
- Create Virtual Environment.
- Start Django Project.
- Write Models.
- MVP for Need creation.
- MVP for Organization creation.
- MVP for Offering creation.
- MVP for Goal creation.
- 

### Week #2
---
- MVP for User dashboard.
- MVP for search Organizations.
- Add an Organization to user.
- Add Users to Organizations.
- Confirm Colour Scheme.
- Implement Mobile First Responsivness.
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






