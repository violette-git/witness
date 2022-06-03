from django.shortcuts import render

from .models import Need
# Create your views here.



def create_need(request):

    # need_list = Need.objects.all()
                         

    return render(request, 'benov_app/need.html')