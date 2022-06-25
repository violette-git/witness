from django.shortcuts import render
from tithe_app.models import Need, Offering
from user_app.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def create(request):

    if not request.user.is_authenticated():

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
        
        return render(request, 'tithe_app/create_need.html')

@login_required
def needsbutton(request):

    context = {

        'needs': Need.objects.all().order_by('-date_created'),
        'users': User.objects.all()
        
    }
    return render(request, 'tithe_app/need.html', context)

@login_required
def contribute(request):

    if request.method == 'GET':
        
        return render(request, 'tithe_app/contribute.html')

    if request.method == 'POST':

        form = request.POST

        amount = form.get('amount')

        contribution = Offering.objects.all()

        # need = contribution.

        # print(need)

        Offering.objects.create(

            amount=amount,
            user=request.user,
            # need=need

        )

        return render(request, 'tithe_app/need.html')
        
