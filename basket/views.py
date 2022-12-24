from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from .basket import Basket
from store.models import Product
# Create your views here.


def basket_content(request ):

    return  render(request ,"basket/basket_content.html")



def basketadd(request):

    basket = Basket(request)


    if request.POST.get('action')=='post':
        p_id=int(request.POST.get("productid"))
        qty=int(request.POST.get("productqty"))
        prod=get_object_or_404(Product,id=p_id)
        basket.add(prod,qty=qty)

        response=JsonResponse({"qty":qty})
    return response

