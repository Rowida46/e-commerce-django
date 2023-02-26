from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def contactView(request):
    return HttpResponse("<h1 >Your Landing Contact Page</h1>")
