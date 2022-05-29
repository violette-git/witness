from django.contrib import admin
from .models import Offering, Tithe
# Register your models here.
admin.site.register([Tithe, Offering])