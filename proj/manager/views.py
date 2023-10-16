from django.http import HttpResponse
from django.shortcuts import render, redirect

# to import models from models.py
from .models import Product, Warehouse

from django.db.models import Sum
from django.urls import reverse

# Create your views here.

# def index(request):
#     params = {'name': 'manager index'}

#     # return HttpResponse("this is index page of warehouse / manager app")
#     return render(request, 'manager/index.html', params)
def index(request):
    total_products_quantity = request.GET.get('total_products_quantity')
    total_warehouse_capacity = request.GET.get('total_warehouse_capacity')
    leftover_capacity = request.GET.get('leftover_capacity')

    products = Product.objects.all()
    context = {
        'total_products_quantity': total_products_quantity,
        'total_warehouse_capacity': total_warehouse_capacity,
        'leftover_capacity': leftover_capacity,
        'products': products,
    }
    
    return render(request, 'manager/index.html', context)

def login(request):

    return render(request, 'manager/managerLogin.html')

def loggedin(request):
        return redirect(login)

    # if(username = "" and passkey = "") :
    #     return render(dashboard)
    # else:
    #     return render(login)

def dashboard(request):
    #query
    total_products_quantity = Product.objects.aggregate(total_quantity=Sum('quantity'))['total_quantity']
    total_warehouse_capacity = Warehouse.objects.aggregate(total_capacity=Sum('capacity'))['total_capacity']
    leftover_capacity = total_warehouse_capacity - total_products_quantity
    
    # Calculate percentage
    percentage_used = (total_products_quantity / total_warehouse_capacity) * 100
    percentage_left = (leftover_capacity / total_warehouse_capacity) * 100

    # Determine if inventory is low
    is_low_inventory = percentage_used >= 90  # Inventory is considered low if 90% or more is used

    # Determine if capacity is full
    is_max_capacity_reached = percentage_left <= 10  # Capacity is considered full if 10% or less is left
    
    context = {
        'total_products_quantity': total_products_quantity,
        'total_warehouse_capacity': total_warehouse_capacity,
        'leftover_capacity': leftover_capacity,
        'is_low_inventory': is_low_inventory,
        'is_max_capacity_reached': is_max_capacity_reached,
    }

    print(context)

    index = reverse('dashboard') + f'?total_products_quantity={total_products_quantity}&total_warehouse_capacity={total_warehouse_capacity}&leftover_capacity={leftover_capacity}'
    return render(request, 'manager/index.html', context)
   
# def index(request):
#     params = {'name': 'manager index'}

#     # return HttpResponse("this is index page of warehouse")
#     return render(request, 'index.html', params)


# def capacity(request):
    total_products_quantity = Product.objects.aggregate(total_quantity=Sum('quantity'))['total_quantity']
    total_warehouse_capacity = Warehouse.objects.aggregate(total_capacity=Sum('capacity'))['total_capacity']
    leftover_capacity = total_warehouse_capacity - total_products_quantity
    
    context = {'total_products_quantity': total_products_quantity,
                'total_warehouse_capacity': total_warehouse_capacity,
                'leftover_capacity':leftover_capacity,}
    print(context)
    index = reverse('/manager/') + f'?total_products_quantity={total_products_quantity}&total_warehouse_capacity={total_warehouse_capacity}&leftover_capacity={leftover_capacity}'

    return redirect(index)
    return render(request, 'manager/index.html', context)
    return render(request, 'manager/capacity.html', context)

def tables(request):    
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'manager/tables-data.html', context)

    return render(request, 'manager/tables-data.html', )