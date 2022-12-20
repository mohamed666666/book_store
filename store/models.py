from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
# Create your models here.




class Category(models.Model):
    name =models.CharField(max_length=255,db_index=True)
    slug=models.SlugField(max_length=255,unique=True)

    class Meta:
        verbose_name_plural= 'Categories'

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("store:categories",args=[self.slug])



class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager,self).get_queryset().filter(isactive=True)

class Product(models.Model):
    category = models.ForeignKey(Category,related_name='product',on_delete=models.CASCADE)
    created_by=models.ForeignKey(User,related_name="product_creator",on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    auther=models.CharField(max_length=255)
    describtion=models.TextField(blank=True)
    img=models.ImageField(upload_to='images/')
    slug=models.SlugField(max_length=255)

    price=models.DecimalField(max_digits=5,decimal_places=2)

    instock=models.BooleanField(default=True)
    isactive=models.BooleanField(default=True)

    created=models.TimeField(auto_now_add=True)
    updated=models.TimeField(auto_now=True)
    objects=models.Manager()
    products=ProductManager()

    class Meta:
        verbose_name_plural= 'Products'
        ordering=('-created',)


    def __str__(self):
        return self.title

    def get_prod_url(self):
        return reverse("store:prod_details",args=[self.slug])


