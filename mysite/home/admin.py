from django.contrib import admin
from .models import Product, Customer, Cart

# Register your models here.

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'dp', 'category', 'product_image']

@admin.register(Customer)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'locality', 'city', 'state', 'zipcode']

@admin.register(Cart)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity']