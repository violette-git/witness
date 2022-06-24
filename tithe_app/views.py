from django.shortcuts import render
from tithe_app.models import Need
from user_app.models import User

# Create your views here.



def create(request):

    if request.method == 'GET':

        return render(request, 'tithe_app/create_need.html')

    if request.method == 'POST':

        form = request.POST

        title = form.get('title')

        type = form.get('type')

        cost = form.get('cost')

        Need.objects.create(
            title=title,
            type=type,
            cost=cost,
            user=request.user
        )

        context = {

        'needs': Need.objects.all().order_by('-date_created')
        
    }

        return render(request, 'tithe_app/need.html', context)



def needsbutton(request):


    context = {

        'needs': Need.objects.all().order_by('-date_created'),
        'users': User.objects.all()
        
    }
    return render(request, 'tithe_app/need.html', context)
        
