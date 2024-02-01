from django.urls import path
from . import views

app_name='start'

urlpatterns = [
    path('', views.start, name='start'),
    path('support/', views.support, name='support'),
    path('payment/', views.payment, name='payment'),
    path('contact/', views.contact, name='contact')
]


