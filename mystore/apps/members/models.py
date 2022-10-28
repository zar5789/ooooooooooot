from unicodedata import category
from django.db import models

# Create your models here.
class stock(models.Model):
    Product_name = models.CharField(max_length=255)
    Category = models.CharField(max_length=255)
    brand_name = models.CharField(max_length=255)
    qty = models.IntegerField()
    price = models.IntegerField()
    picture = models.ImageField()
    