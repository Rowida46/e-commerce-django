from django.shortcuts import reverse, get_object_or_404
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
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


class Edit_Category(View):
    def get(self, request, id):
        cat = Categories.get_spesific_category(id)
        form = CreateForm(instance=cat)
        return render(request, "categories/create_Category.html", context={"form": form})

    def post(self, request, id):
        cat = Categories.get_spesific_category(id)
        category = CreateForm(request.POST, request.FILES, instance=cat)
        if category.is_valid():
            category.save()
            return redirect("get_cats")
        else:
            return redirect("create_cat")


class Delete_Category(View):
    def get(self, request, id):
        cat = Categories.get_spesific_category(id)
        return redirect("get_cats")

    def post(self, request, id):
        cat = Categories.get_spesific_category(id)
        cat.delete()
        return redirect('get_cats')


# using generic list view ->>>>>>>>>>>>>>>>>>>


class list_cats(ListView):
    """
    a generic class based view that hold 
        1- model  -> model name
        2- template -> html template page
    """

    """
    Specifying model = Publisher is shorthand for saying
      queryset = Publisher.objects.all(). However
    """
    model = Categories

    """note : if we dnt spesify `context_object_name`
    -> retreving data in template would be via obj called
        `object_list`
    """
    context_object_name = "cats"
    template_name = "categories/lst_Categories.html"


class create_Cat(CreateView):
    model = Categories
    template_name = "categories/create_Category.html"
    form_class = CreateForm
    success_url = "/categories/get_Categories"


"""

success_url -> hold route -> not template rel path

"""


class ModelDetailView(DetailView):

    model = Categories
    context_object_name = "Category"
    template_name = 'categories/category_detail.html'


class ModelUpdateView(UpdateView):
    model = Categories
    template_name = "categories/create_Category.html"
    form_class = CreateForm

    def get_success_url(self):
        return reverse('show_cat', kwargs={'pk': self.object.pk})

    # success_url = reverse('show_cat',  kwargs={'pk': self.object.pk})


class CategoryDeleteView(DeleteView):
    model = Categories
    template_name = 'categories/delete.html'
    success_url = "/categories/get_Categories"
