from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    # params = {'name': 'client index'}

    # return HttpResponse("this is index page of warehouse / client app")
    return render(request, 'client/index.html')

# def index(request):
#     params = {'name': 'manager index'}

#     # return HttpResponse("this is index page of warehouse")
#     return render(request, 'index.html', params)