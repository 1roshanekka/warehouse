# made urls.py file for admin app

# from django.contrib import admin
# not required as we are accessing from creted app
from django.urls import path, include

from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name="index"),

    # path('login/', views.login, name="managerLogin"),
    path('dashboard/', views.dashboard, name="dashboard"),
    # path('capacity/', views.capacity, name='capacity'),


    path('tables/', views.tables, name="tables"),
    path('addProducts/', views.addProducts, name="addProducts"),
    path('submit_product_form/', views.submit_product_form, name='submit_product_form'),
    # path('about/', views.about, name="about"),
    # path('services/', views.services, name="services"),
    # path('contact/', views.contact, name="contact"),

    # ... (other patterns)
    path('products/<int:product_id>/edit/', views.edit_product, name='edit_product'),
    path('manager/get_stock_data/', views.get_stock_data, name='get_stock_data'),
]


