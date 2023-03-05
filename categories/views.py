from django.shortcuts import render

# Create your views here.

from .models import Categories


def get_cats():
    categories = Categories.get_all_categories()
    