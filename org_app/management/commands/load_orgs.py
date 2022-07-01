import requests

from django.core.management.base import BaseCommand

from org_app.models import Organization

import json

class Command(BaseCommand):

    def handle(self, *args, **options):
        
        Organization.objects.all().delete()

        BASE_URL = "https://api.data.charitynavigator.org/v2/Organizations?app_id=10455753&app_key=fec10e649e30363784b4517a00db4408&pageSize=1000"

        response = requests.get(BASE_URL, headers={'Accept': 'application/json'})

        data = json.loads(response.text)

        for i in range(len(data)):

            business_name = data[i]['charityName']
            mission_statement = data[i]['mission']
            website_url = data[i]['websiteURL']
            tagline = data[i]['tagLine']
            address = data[i]['mailingAddress']['streetAddress1']
            city = data[i]['mailingAddress']['city']
            state = data[i]['mailingAddress']['stateOrProvince']

            Organization.objects.create(

                business_name = business_name,
                address = address,
                city = city,
                state = state,
                website_url = website_url,
                mission_statement = mission_statement,
                tagline = tagline,
            )