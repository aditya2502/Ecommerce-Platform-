from django.db import models
from base.models import BaseModel

# Create your models here.

class Catagory(BaseModel):
    catagory_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,null = True,blank =True)
    catagory_image= models.ImageField(upload_to='catagories')
    
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.TextField(max_length=100)
    catagory= models.ForeignKey(Catagory,on_delete=models.CASCADE,related_name='products')
    price = models.IntegerField()
    
class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='product_images')
    image = models.ImageField(upload_to='products')
    
    
