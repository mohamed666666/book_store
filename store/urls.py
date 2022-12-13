from django.urls import path

from . import views

app_name="store"

urlpatterns = [

    path("",views.home,name='home'),
    path("item/<slug:slug>/",views.product_details,name='prod_details'),
    path("cat/<slug:slug>/",views.list_cats,name='categories')
]