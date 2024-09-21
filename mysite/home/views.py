from django.shortcuts import render
from django.views import View
from django.db.models import Count
from .models import Product

# Create your views here.

def home(request):
    return render(request, 'home/home.html')

class CategoryView(View):
    def get(self, request, val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request, 'home/category.html', locals())

class ProductDetail(View):
    def get(self, request, pk):
        return render(request, 'home/productdetail.html', locals())