from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    params = {'name': 'manager index'}

    # return HttpResponse("this is index page of warehouse / manager app")
    return render(request, 'manager/index.html', params)

# def index(request):
#     params = {'name': 'manager index'}

#     # return HttpResponse("this is index page of warehouse")
#     return render(request, 'index.html', params)