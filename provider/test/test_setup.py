from rest_framework.test import APITestCase
from django.urls import reverse


class TestSetup(APITestCase):
    def setUp(self):
        self.providers_url='/providers/'
        self.servicearea_url = '/servicearea/'
        self.loc_providers_url = reverse('loc-providers')

        # providers data
        self.provider_data = {
            'name': "Test Provider",
            'email': "testprovider@email.com",
            'phone_no': "445677888",
            'language': "aa",
            'currency': "XUA",
        }
        
        # Service Area data
        self.service_area_data = {
            'name': 1,
            'price': "1000.00",
            'location': "{'type': 'Polygon', 'coordinates': [[0.0, 0.0], [1.0, 1.0]]}",
        }
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()
