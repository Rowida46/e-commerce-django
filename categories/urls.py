from django.contrib import admin
from django.urls import path
from categories.views import *


urlpatterns = [
   path("get_Categories" , get_Categories.as_view() , name="get_cats"),
   path("create_Category" , create_Category.as_view() , name="create_cat")

]