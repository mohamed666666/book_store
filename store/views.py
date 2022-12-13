from django.shortcuts import render , get_object_or_404
from .models import Category,Product
# Create your views here.
def home(request):
    context = {"products": Product.objects.all()}
    return  render(request,'store/home.html',context)



def product_details(request,slug ):
    product=get_object_or_404(Product,slug=slug,instock=True)
    return render(request,"store/product.html",{"product":product})




def list_cats(request,slug):
    categories=get_object_or_404(Category,slug=slug)
    prods=Product.objects.filter(category=categories)
    return render(request,"store/categories.html",{"cat":categories,"prods":prods})




def categories(request):
     return  {"categories":Category.objects.all()}
