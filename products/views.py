from categories.models import *
from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpResponse, HttpResponseNotFound

from products.ProductForm import *
from .models import Products
from django.db.models import Avg

import requests
import json


# response_API = requests.get('https://dummyjson.com/products')
# print(response_API.json())

# users staff
with open("products/data.json") as json_file:
    products = json.load(json_file)


def productView(request):
    return HttpResponse('<h1> your landing home for products  </h1>')


def lst_products(request, db_products=[]):
    db_products = Products.get_all_products() if db_products == [] else db_products
    products_num = Products.get_products_count()

    db_products = db_products.order_by("-created_at")
    return render(request, "products/products_details_view.html", context={"products": db_products, "counts": products_num})


"""

def product_details(request, id):
    for prod in products:
        if (prod["id"] == id):
            return render(request, "products/product_view.html", context={"prod": prod})
    msg = "we run out of stock, your product not found "
    # return HttpResponseNotFound(<h1>product not found </h1>)
    return render(request, "not_found.html", context={"msg": msg})
 """


def product_details_by_slung(request, slug):
    # prod = get_object_or_404(Products, pk=id)
    prod = Products.get_spefic_product_by_slug(slug)
    return render(request, "products/product_view.html", context={"prod": prod})


def product_details(request, id):
    prod = Products.get_product(id)
    cats = Products.objects.filter(category=prod.category).order_by("-rate") # des
    count = cats.count() - 1
    avg = round(cats.aggregate(Avg("rate"))["rate__avg"], 2)
    print(avg, count)
    if prod:
        return render(request, "products/product_view.html", context={"prod": prod, "cats": cats, "avg_rate": avg, "count": count})
    msg = "we run out of stock, your product not found "
    # return HttpResponseNotFound(<h1>product not found </h1>)
    return render(request, "not_found.html", context={"msg": msg})


def search_by_title(request, title):
    res = Products.filter_products(title)
    return redirect('lst_products')


def index(request):
    return render(request, "index.html")


def not_found(request, msg="now"):
    return render(request, "not_found.html", context={"msg": msg})


""" for prd in products[:5]:
    cat = Categories(name = prd["category"])
    cat.save()
    tmp = Products(title=prd["title"],
                   price=prd["price"], description=prd["description"],
                   stock=prd["stock"],
                   rate=prd["rating"])
    tmp.save() """


def deleteProduct(request, id):
    # post = Post.objects.get(id=id)
    prd = get_object_or_404(Products, pk=id)
    prd.delete()
    # return render(request, 'posts/show.html', context={"post": post})
    # return HttpResponse("post deleted")
    return redirect('lst_products')


def create_product(request):
    if request.method == 'GET':
        newProductForm = ProductModelForm()
        return render(request, 'products/createform.html', context={'form': newProductForm})

    elif request.method == 'POST':
        newProductForm = ProductModelForm(request.POST, request.FILES)
        if newProductForm.is_valid():
            newProductForm.save()
            return redirect("lst_products")
        return redirect('create_product')
    return redirect("lst_products")


def edit_product(request, id):
    product = Products.get_product(id)
    if request.method == 'GET':
        ProductForm = ProductModelForm(instance=product)
        return render(request, 'products/createform.html', context={'form': ProductForm})

    elif request.method == 'POST':
        editedProduct = ProductModelForm(
            request.POST, request.FILES, instance=product)
        if editedProduct.is_valid():
            editedProduct.save()
            return redirect("lst_products")
        return redirect('edit_product')

    return redirect("lst_products")
