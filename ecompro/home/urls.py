
from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.all_prod_cat, name='all_prod_cat'),
    path('<slug:c_slug>/', views.all_prod_cat, name='Products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='prodCatdetail'),


]








