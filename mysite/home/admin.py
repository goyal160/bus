from django.contrib import admin
from .models import Product

# Register your models here.

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'dp', 'category', 'product_image']