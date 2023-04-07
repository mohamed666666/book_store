from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .Forms import OrderForm
from .models import order ,OrderItem
from basket.basket import Basket
# Create your views here.
from django.http.response import JsonResponse



@login_required
def placeorder(request):
    basket = Basket(request)
    
    if request.method=="POST":
        user_id = request.user.id
        of=OrderForm(request)
       
        if of.is_valid:
             pass
        order_creator_name=request.POST["fullname"]
        city=request.POST["City"]
        address=request.POST["address"]
        Phone=request.POST["Phone"]

        
        ord=order.objects.create(user_id=user_id,full_name=order_creator_name,address1=address,address2=address,
                                    city=city,phone=Phone,total_paid=basket.get_total_paid())
        order_id = ord.pk
        prods,qts=basket.get_products()
        for p ,q in zip(prods,qts):
                
                OrderItem.objects.create(order_id=order_id, product=p, price=p.price, quantity=q)
    else:
        of=OrderForm()


    response = JsonResponse({'success': 'Return something'})
    return redirect('user:dashboard')



@login_required
def showing_orders(request):
     pass