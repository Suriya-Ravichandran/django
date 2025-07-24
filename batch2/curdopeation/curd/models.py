from django.db import models

# Create your models here.
class Product(models.Model):
    productname=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    productprice=models.CharField(max_length=100)
    productdist=models.CharField(max_length=100)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)  # <-- Add this


    def __str__(self):
        return self.productname
