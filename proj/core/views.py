# created this views.py file


from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name': 'Roshan'}

    return HttpResponse("<a href='/manager'>Manager</a><br><a href='/client'>Client</a><br><a href='/admin'>Admin</a>")
    return render(request, 'index.html', params)
