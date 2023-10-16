from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import ContactForm

# Create your views here.

def index(request):
    # params = {'name': 'client index'}

    # return HttpResponse("this is index page of warehouse / client app")
    return render(request, 'client/index.html')

# def index(request):
#     params = {'name': 'manager index'}

#     # return HttpResponse("this is index page of warehouse")
#     return render(request, 'index.html', params)

def submit_form(request):
    if request.method == 'POST':
        print(request)
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        print(name,email,subject,message)

    return render(request, 'index.html', name,email,subject,message)
# def submit_form(request):
#     if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             subject = form.cleaned_data['subject']
#             message = form.cleaned_data['message']

#             # Assuming you have a model named ContactForm
#             ContactForm.objects.create(name=name, email=email, subject=subject, message=message)

#     # Render the form on GET request or if the form is invalid
#     return render(request, 'index.html', {'form': ContactForm()})
