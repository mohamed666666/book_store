from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from .basket import Basket
from store.models import Product
# Create your views here.


def basket_content(request ):
    basket = Basket(request)
    prods,qs,  prices =basket.get_products()
    out=zip(prods,qs)

    context={"out":out,"total":prices+11.50,"subtotal":prices}



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
        _,_,prices=basket.get_products()
        bas_count = basket.__len__()
        response = JsonResponse({"qty": bas_count,"subtotal":prices})
    return response







def basket_update(request):
    basket = Basket(request)
    prods, _ , prices = basket.get_products()

    if request.POST.get('action') == 'post':
        p_id = int(request.POST.get("productid"))
        product_qty=int(request.POST.get("productqty"))
        basket.update(p_id,product_qty)

        bas_count = basket.__len__()
        response = JsonResponse({"qty": bas_count,"subtotal":prices})
    return response