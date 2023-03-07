from django.contrib import admin
from django.urls import path
from categories.views import *


urlpatterns = [
    # path("get_Categories", get_Categories.as_view(), name="get_cats"),
    # path("create_Category", create_Category.as_view(), name="create_cat"),

    path("get_Categories", list_cats.as_view(), name="get_cats"),
    path("create_Category", create_Cat.as_view(), name="create_cat"),
    # path("<int:id>/edit", Edit_Category.as_view(), name="edit_cat"),
    path("<int:pk>/edit", ModelUpdateView.as_view(), name="edit_cat"),

    path("<int:id>/delete", Delete_Category.as_view(), name="delete_cat"),
    path("<int:pk>", ModelDetailView.as_view(), name="show_cat")

]
