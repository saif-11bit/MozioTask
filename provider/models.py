from django.db import models
from djgeojson.fields import PolygonField
from languages.fields import LanguageField
from djmoney.models.fields import CURRENCY_CHOICES

class Provider(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_no = models.IntegerField()
    language = LanguageField(max_length=100)
    currency = models.CharField(max_length=255, choices=CURRENCY_CHOICES, default='USD')
    
    def __str__(self):
        return self.name


class ServiceArea(models.Model):
    name = models.ForeignKey(Provider, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = PolygonField()

    def __str__(self):
        return self.name.name
