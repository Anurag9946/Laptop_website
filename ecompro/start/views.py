from django.shortcuts import render

# Create your views here.

def start(request):
    return render(request, 'start.html')

def support(request):
    return render(request, 'support.html')

def payment(request):
    return render(request, 'payment.html') 

def contact(request):
    return render(request, 'contact.html')