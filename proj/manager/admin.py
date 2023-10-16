from django.contrib import admin

# Register your models here.
from .models import Product
from .models import Warehouse
from django.db.models import Sum


# Assuming you have a Warehouse model with 'capacity' field and a Product model with specified fields

class ProductList(admin.ModelAdmin):
    list_display = ('name', 'products_status', 'quantity', 'arrival_date', 'dispatch_date')

admin.site.register(Product, ProductList)

class WarehouseView(admin.ModelAdmin):
    def leftover_capacity(self, obj):
        total_products_quantity = Product.objects.aggregate(total_quantity=Sum('quantity'))['total_quantity']
        return obj.capacity - total_products_quantity
    
    list_display = ('name', 'location', 'capacity', 'leftover_capacity')

admin.site.register(Warehouse, WarehouseView)