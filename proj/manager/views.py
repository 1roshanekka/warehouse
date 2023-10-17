from datetime import date

from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render, redirect

# to import models from models.py
from .models import Product
from .models import Warehouse

from django.db.models import Sum
from django.urls import reverse

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

    current_date = date.today()

    # Query for current stock
    current_stock = Product.objects.filter(arrival_date__lte=current_date, dispatch_date__gte=current_date)

    # Query for upcoming stock
    upcoming_stock = Product.objects.filter(arrival_date__gt=current_date)

    # Query for current stock and get the sum of quantities
    current_stock_sum = Product.objects.filter(arrival_date__lte=current_date, dispatch_date__gte=current_date).aggregate(total_quantity=Sum('quantity'))['total_quantity'] or 0

    # Query for upcoming stock and get the sum of quantities
    upcoming_stock_sum = Product.objects.filter(arrival_date__gt=current_date).aggregate(total_quantity=Sum('quantity'))['total_quantity'] or 0

    context = {
        'total_products_quantity': total_products_quantity,
        'total_warehouse_capacity': total_warehouse_capacity,
        'leftover_capacity': leftover_capacity,
        'is_low_inventory': is_low_inventory,
        'is_max_capacity_reached': is_max_capacity_reached,
        'current_stock': current_stock,
        'upcoming_stock': upcoming_stock,
        'current_stock_sum': current_stock_sum,
        'upcoming_stock_sum': upcoming_stock_sum,
    }

    print(context)

    index = reverse('dashboard') + f'?total_products_quantity={total_products_quantity}&total_warehouse_capacity={total_warehouse_capacity}&leftover_capacity={leftover_capacity}&current_stock={current_stock}&upcoming_stock={upcoming_stock}&upcoming_stock_sum={upcoming_stock_sum}&current_stock_sum={current_stock_sum}'
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

from django.shortcuts import render, get_object_or_404

def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        # Update product data
        product.name = request.POST.get('name')
        product.category = request.POST.get('category')
        product.SKU = request.POST.get('SKU')
        product.quantity = request.POST.get('quantity')
        product.arrival_date = request.POST.get('arrival_date')
        product.dispatch_date = request.POST.get('dispatch_date')
        product.save()

        return redirect('product_detail', product_id=product_id)  # Redirect to product detail view

    context = {'product': product}
    return render(request, 'manager/edit-form.html', context)
from django.http import JsonResponse

def get_stock_data(request):
    # Query your Django models to get the necessary data
    # Assuming you have the data in two lists: current_stock and upcoming_stock
    current_stock = [10, 15, 8, 20, 12]
    upcoming_stock = [5, 8, 12, 6, 10]
    dates = ["Date 1", "Date 2", "Date 3", "Date 4", "Date 5"]

    data = {
        'series': [
            {'name': 'Current Stock', 'data': current_stock},
            {'name': 'Upcoming Stock', 'data': upcoming_stock}
        ],
        'dates': dates
    }

    return JsonResponse(data)