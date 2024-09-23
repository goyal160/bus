from django.shortcuts import render
from django.views import View
from django.db.models import Count
from .models import Product, Customer
from . forms import CustomerRegistrationForm, CustomerProfileForm
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
        form = CustomerProfileForm()
        return render(request, 'home/profile.html', locals())
    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']

            reg = Customer(user=user, name=name, locality=locality, city=city, mobile=mobile, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request, "Hey! You're ready to order.")
        else:
            messages.warning(request, "Invalid data entry. Please try again.")
        return render(request, 'home/profile.html', locals())

def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'home/address.html', locals())