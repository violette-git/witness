from django.contrib import admin

from org_app.models import Organization, Goal
# Register your models here.
admin.site.register([Organization, Goal])
