from django.shortcuts import render, redirect
from .forms import ItemForm
from .models import Item


def add_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("items")
    else:
        form = ItemForm()

    return render(request, "catalog/add.html", {"form": form})


def list_items(request):
    items = Item.objects.order_by("-created_at")
    print("SERVER ITEM COUNT:", items.count())
    return render(request, "catalog/items.html", {"items": items})