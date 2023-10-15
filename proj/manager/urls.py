# made urls.py file for admin app

# from django.contrib import admin
# not required as we are accessing from creted app
from django.urls import path, include

from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name="managerHome"),
    # path('about/', views.about, name="about"),
    # path('services/', views.services, name="services"),
    # path('contact/', views.contact, name="contact"),

]
