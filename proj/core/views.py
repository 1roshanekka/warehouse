# created this views.py file


from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name': 'Roshan'}

    # return HttpResponse("this is index page of warehouse")
    return render(request, 'index.html', params)
  
def about(request):
    return HttpResponse("this is about page of warehouse")

def services(request):
    return HttpResponse("this is services page of warehouse")

def contact(request):
    return HttpResponse("this is contact page of warehouse")

def dashboard(request):
    return HttpResponse("this is dashboard page of warehouse")
