from .test_setup import TestSetup
from provider.models import Provider, ServiceArea

class TestViews(TestSetup):
    
    # test post request to provider
    def test_provider_cannot_be_creater(self):
        res = self.client.post(self.providers_url)        
        self.assertEqual(res.status_code, 400)


    def test_provider_can_be_created(self):
        res = self.client.post(self.providers_url, self.provider_data, format='json')        
        self.assertEqual(res.status_code, 201)
        
    #test get request to provider
    def test_get_provider(self):
        res = self.client.get(self.providers_url)        
        self.assertEqual(res.status_code, 200)
        

    #test put request to provider
    def test_put_provider(self):
        response = self.client.post(self.providers_url, self.provider_data, format='json')
        id = response.data['id']
        provider = Provider.objects.get(id=id)
        provider.name='sec provider'
        provider.email='sec@email.com'
        provider.phone_no=38484844
        provider.save()
        url = f"{self.providers_url}{id}/"
        res = self.client.put(url,self.provider_data)
        self.assertEqual(res.status_code, 200)
        
        
        
    # test post request to service area
    def test_service_area_cannot_be_creater(self):
        res = self.client.post(self.servicearea_url)        
        self.assertEqual(res.status_code, 400)


    def test_service_can_be_created(self):
        response = self.client.post(self.providers_url, self.provider_data, format='json')
        id = response.data['id']
        service_area_data = {
            'name': id,
            'price': "1000.00",
            'location': "{'type': 'Polygon', 'coordinates': [[0.0, 0.0], [1.0, 1.0]]}",
        }
        res = self.client.post(self.servicearea_url, service_area_data, format='json')        
        self.assertEqual(res.status_code, 201)
        
    #test get request to service area
    def test_get_service_area(self):
        res = self.client.get(self.servicearea_url)        
        self.assertEqual(res.status_code, 200)
        

    #test put request to service are
    def test_put_provider(self):
        response = self.client.post(self.providers_url, self.provider_data, format='json')
        prov_id = response.data['id']
        service_area_data = {
            'name': prov_id,
            'price': "1000.00",
            'location': "{'type': 'Polygon', 'coordinates': [[0.0, 0.0], [1.0, 1.0]]}",
        }
        resp = self.client.post(self.servicearea_url, service_area_data, format='json') 
        id = resp.data['id']
        service_area = ServiceArea.objects.get(id=id)
        service_area.price="2000.00"
        service_area.location="{'type': 'Polygon', 'coordinates': [[0.0, 0.0], [1.0, 1.0], [2.0, 2.0]]}"
        service_area.save()
        url = f"{self.servicearea_url}{id}/"
        res = self.client.put(url,service_area_data)
        self.assertEqual(res.status_code, 200)
        
