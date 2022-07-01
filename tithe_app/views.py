from django.shortcuts import render, get_object_or_404, redirect
from tithe_app.models import Need, Offering
from user_app.models import User
from django.contrib.auth.decorators import login_required
from decimal import Decimal

# Create your views here.


@login_required
def create(request):

    if not request.user.is_authenticated:

        return render(request, 'user_app/login.html')


    elif request.method == 'POST':

        form = request.POST

        title = form.get('title')

        type = form.get('type')

        cost = form.get('cost')

        description = form.get('description')

        Need.objects.create(
            title=title,
            type=type,
            cost=cost,
            user=request.user,
            description=description
        )

        context = {

        'needs': Need.objects.all().order_by('-date_created')
        
        }

        return render(request, 'tithe_app/need.html', context)

    else:

        context = {

        'needs': Need.objects.all().order_by('-date_created')
        
        }
        
        return render(request, 'tithe_app/need.html', context)





@login_required
def needsbutton(request):

    context = {

        'needs': Need.objects.all().order_by('-date_created'),
        'users': User.objects.all()
        
    }
    return render(request, 'tithe_app/need.html', context)



    



def need_details(request, need_id):

    need = get_object_or_404(Need, pk=need_id)   
    

    context = {
        
        'need':need,
        'needs': Need.objects.all().order_by('-date_created'),
        'users': User.objects.all(),
    }

    
    
    return render(request, 'tithe_app/need_details.html', context)





@login_required
def contribute(request, need_id):

    need = get_object_or_404(Need, pk=need_id)

    context = {

        'need':need
    }

    if request.method == 'GET':
        
        
        return render(request, 'tithe_app/contribute.html', context)

    if request.method == 'POST':

        form = request.POST

        amount = Decimal(form.get('amount'))

        # do logic for entering a string

        # is_tithe = form.get('is_tithe')

        context = {

        'need':need,
        'needs': Need.objects.all().order_by('-date_created'),
        'users': User.objects.all(),
        }
        
        Offering.objects.create(

            amount=amount,
            user=request.user,
            need=need,

            # is_tithe=is_tithe

        )

        need.donated_amount += amount

        need.save()

        return redirect('tithe_app:create')
        
