from django.shortcuts import render
import requests
from django.template import engines


# Create your views here.



def base(request):

    return render(request, 'base.html')

def whereami(request):
	if request.method == 'GET':
		
		url = "https://www.google.com/maps/dir/?api=1"
		payload = ""
		headers = {
		}
		
		# url2 = "https://www.google.com/recaptcha/api/siteverify"


		response = requests.request("GET", url, headers=headers, data=payload)
		# print(response.text)
		html = response.text
		# print(html)
		django_engine = engines['django']
		template = django_engine.from_string(html)
		# test = lxml.html.fromstring(f'{html}')
		# print(template.render(), 'templates', '----------------------------------------------')
		
		context = {
			'response': template.render()
		}
		template.render(context)
		return render(request, 'whereami.html', context)