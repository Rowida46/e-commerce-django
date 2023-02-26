from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def contactView(request):
    return HttpResponse("<h1 >Your Landing Contact Page</h1>")



def contactUs(request):
    return render(request, 'contact/contactUs.html')


def aboutUs(request):
    return render(request, "contact/aboutUs.html")
