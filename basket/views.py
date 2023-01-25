from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from .basket import Basket
from store.models import Product
# Create your views here.


def basket_content(request ):
    basket = Basket(request)
    prods,qs=basket.get_products()
    out=zip(prods,qs)
    context={"out":out}



    return  render(request ,"basket/basket_content.html",context)



def basketadd(request):

    basket = Basket(request)


    if request.POST.get('action')=='post':
        p_id=int(request.POST.get("productid"))
        qty=int(request.POST.get("productqty"))
        prod=get_object_or_404(Product,id=p_id)
        basket.add(prod,qty=qty)

        bas_count=basket.__len__()
        response=JsonResponse({"qty":bas_count})
    return response

def basketdelete(request):
    basket = Basket(request)

    if request.POST.get('action') == 'post':
        p_id = int(request.POST.get("productid"))

        basket.delete(p_id)

        bas_count = basket.__len__()
        response = JsonResponse({"qty": bas_count})
    return response