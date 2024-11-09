from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product

class ProductListView(ListView):
    model = Product

class ProductDetailView(DetailView):
    model = Product
    fields = '__all__'


