from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import (
    login as django_login,
    logout as django_logout,
    authenticate,
    get_user_model 
)

from .models import User

# Create your views here.
def base(request):

    return render(request, 'base.html')


def register(request):

    if request.method == 'GET':
    
        return render(request, 'user_app/register.html')
    
    elif request.method == 'POST':

        form = request.POST

        username = form.get('username')

        password = form.get('password')

        first_name = form.get('first-name')

        last_name = form.get('last-name')

        email = form.get('email')

        user = User.objects.create_user(

            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
            password=password,
            
        )

        django_login(request, user)

        return redirect(reverse('user_app:profile', kwargs={ 'username': user.username}))    

# --------------------------------------------------------

def login(request):

    if request.method == 'GET':

        return render(request, 'user_app/login.html')

    elif request.method == 'POST':

        form = request.POST

        username = form.get('username')

        password = form.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:

            django_login(request, user) 

        return redirect(reverse('user_app:profile', kwargs={ 'username': user.username}))




# --------------------------------------------------------
@login_required
def profile(request, username):

    if request.method == 'GET':

        user = get_object_or_404(get_user_model(), username=username)

        context = {

            'username': request.user,
            
        }

        return render(request, 'user_app/mem-dashboard.html', context)



# --------------------------------------------------------

def logout(request):

    django_logout(request)

    return redirect('user_app:base')

# ----------------------------------------------------------------------------

def test(request):

    return render(request, 'test.html')

