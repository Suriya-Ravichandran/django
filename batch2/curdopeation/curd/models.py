from django.db import models

# Create your models here.
class Product(models.Model):
    productname=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    productprice=models.CharField(max_length=100)
    productdist=models.CharField(max_length=100)


    def __str__(self):
        return self.productname
