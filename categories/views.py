from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

# Create your views here.

from .models import Categories
from .craeteForm import CreateForm


def get_cats():
    categories = Categories.get_all_categories()


class get_Categories(View):
    # we need to handle http requests
    def get(self, request):
        cats = Categories.get_all_categories().order_by("-created_at")
        return render(request, "categories/lst_Categories.html", context={"cats": cats})


class create_Category(View):
    def get(self, request):
        form = CreateForm()
        return render(request, "categories/create_Category.html", context={"form": form})

    def post(self, request):
        category = CreateForm(request.POST, request.FILES)
        if category.is_valid():
            category.save()
            return redirect("get_cats")
        else:
            return redirect("create_cat")
