from django.shortcuts import render
from django.http import HttpResponse


# https://dummyjson.com/products


import requests
import json


# response_API = requests.get('https://dummyjson.com/products')
# print(response_API.json())

# users staff
with open("products/data.json") as json_file:
    products = json.load(json_file)


def productView(request):
    return HttpResponse('<h1> your landing home for products  </h1>')


def lst_products(request):
    return render(request, "products/products_details_view.html", context={"products": products})


def product_details(request, id):

    for prod in products:
        if (prod["id"] == id):
            return render(request, "products/product_view.html", context={"prod": prod})
    return HttpResponse("<h1>product not found <h1/>")

