from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


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
    msg = "we run out of stock, your product not found "
    #return HttpResponseNotFound(<h1>product not found </h1>)
    return render(request, "not_found.html", context= {"msg" : msg})


def index(request):
    return render(request, "index.html")

def not_found(request, msg="now"):
    return render(request, "not_found.html", context={"msg" : msg})