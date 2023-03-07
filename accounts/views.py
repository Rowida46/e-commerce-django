from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.models import User
from accounts.RegisterForm import *
from django.views import View


# Create your views here.

class Register(CreateView):
    model = User
    # form_class = UserCreationForm
    form_class = RegistrationForm
    template_name = "accounts/register.html"
    success_url = "/products/products"


class ProfileView(View):
    def get(self, request):
        # return HttpResponse('--- Welcome to your profile ----')
        return redirect('lst_products')

class LogOut(View):

    def get(self,request):
        print("pppppppppppppp")
        return redirect("home")

