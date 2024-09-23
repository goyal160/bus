from django.shortcuts import render
from django.views import View
from django.db.models import Count
from .models import Product
from . forms import CustomerRegistrationForm
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')

class CategoryView(View):
    def get(self, request, val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request, 'home/category.html', locals())

class CategoryTitle(View):
    def get(self, request, val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request, 'home/category.html', locals())

class ProductDetail(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'home/productdetail.html', locals())
    
class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'home/customer_registration.html', locals())
    
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Welcome on board!")
        else:
            messages.warning(request, "Invalid data entry")
        return render(request, 'home/customer_registration.html', locals())
    
class ProfileView(View):
    def get(self, request):
        return render(request, 'home/profile.html', locals())
    def post(self, request):
        return render(request, 'home/profile.html', locals())