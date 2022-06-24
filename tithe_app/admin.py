from django.contrib import admin
from .models import Offering, Need
# Register your models here.
admin.site.register([Offering, Need])