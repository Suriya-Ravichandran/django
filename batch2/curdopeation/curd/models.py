from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name= models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Create your models here.
class Product(models.Model):
    productname=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    productprice=models.CharField(max_length=100)
    productdist=models.CharField(max_length=100)
    quantity=models.CharField(max_length=100)
    create_at=models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(unique=True)
    category= models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)  # <-- Add this

    def save(self, *args,**kwargs):
        self.slug = slugify(self.productname)
        super().save( *args,**kwargs)


    def __str__(self):
        return self.productname

