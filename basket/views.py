from django.shortcuts import render

# Create your views here.


def basket_content(request ):
    return  render(request ,"basket/basket_content.html")