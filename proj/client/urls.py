# made urls.py file for admin app

# from django.contrib import admin
# not required as we are accessing from creted app
from django.urls import path, include

from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import submit_form

urlpatterns = [

    # in-> views.{function defined in views.py}

    path('', views.index, name="client-Home"),
    path('submit_form/', views.submit_form, name='client-submit_form'),
]
