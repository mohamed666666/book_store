from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name="store"

urlpatterns = [

    path("",views.home,name='home'),
    path("item/<slug:slug>/",views.product_details,name='prod_details'),
    path("cat/<slug:slug>/",views.list_cats,name='categories')
]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)