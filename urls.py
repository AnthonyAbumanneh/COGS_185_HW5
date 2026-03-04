from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.add_item, name="add"),
    path("items/", views.list_items, name="items"),
]