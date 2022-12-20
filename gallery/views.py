from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView
)
from django.views.generic import TemplateView
from .forms import CollectionForm, ItemForm
from .models import Collection

# Create your views here.


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


def collection_view(request):

    collections = Collection.objects.all()

    if request.method == 'POST':
        form = CollectionForm(request.POST, request.FILES)
        itemForm = ItemForm()
        if form.is_valid():
            form.save()
            collection_obj = form.instance
            return render(request, 'pages/collection.html', {'form': form, 'collection_obj': collection_obj, 'collections': collections, 'itemForm': itemForm, })

    else:
        form = CollectionForm()
        itemForm = ItemForm()
    return render(request, 'pages/collection.html', {'form': form, 'itemForm': itemForm, 'collections': collections})


class CollectionDetailView(DetailView):
    model = Collection
    template_name = 'pages/collection_detail.html'


def item_view(request):

    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            item_obj = form.instance
            return redirect('collection')

    else:
        return redirect('collection')
