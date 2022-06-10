from django.shortcuts import get_object_or_404, render, redirect
from django.shortcuts import render
from .models import Organization
from django.urls.base import reverse
from django.contrib.auth import (
    get_user_model,
)

# Create your views here.
def create_org(request):

    if request.method == 'GET':

        form = request.GET

        return render(request, 'org_app/register-org.html' )

    elif request.method == 'POST':

        form = request.POST

        business_name = form.get('business_name')

        website_url = form.get('website_url')

        facebook_url = form.get('facebook_url') 

        mission_statement = form.get('mission_statement')

        is_nonprofit = form.get('is_nonprofit')     

        organization = Organization.objects.create(

            business_name = business_name,
            website_url = website_url,
            facebook_url = facebook_url,
            mission_statement = mission_statement,
            is_nonprofit =  is_nonprofit
        )

        print(organization)

        return redirect(reverse('user_app:profile', args=[request.user.username, ]))

def orgs(request):

    organizations = Organization.objects.all()

    context = {

        'organizations':organizations,
    }

    if request.method == 'GET':

        return render(request, 'mem-dashboard.html', context)



    return render(request, 'mem-dashboard.html', context)