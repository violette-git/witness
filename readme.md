# Transparency Giving App (witness)
---
## **Overview**
---
## **Features**
---
### Tasks:
- ihihini
- khvkiugc
- yfxku,yrkvku
- iydikytxlutyd
### Additional Features

- iufyiuf
- khgcdiytdc
- igiytf
## Data Models
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


