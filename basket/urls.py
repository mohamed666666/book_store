from django.urls import path

from . import views
app_name="basket"


urlpatterns = [

    path("",views.basket_content,name='basket_content'),
    path("adding/",views.basketadd,name='basket_add'),
    path("delete/",views.basketdelete,name='basket_delete')


]