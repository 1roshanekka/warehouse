from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render,redirect
from client.models import ContactForm


# Create your views here.

def index(request):
    # params = {'name': 'client index'}
    # return HttpResponse("this is index page of warehouse / client app")

    return render(request, 'client/index.html')

# submit from index page
def submit_form(request):
    if request.method == 'POST':
        print(request)
        submitted_name = request.POST.get('name') #name from html
        submitted_email = request.POST.get('email')
        submitted_subject = request.POST.get('subject')
        submitted_message = request.POST.get('message')

        # below is to be stored in name section of model-ContactForm
        details = ContactForm(name=submitted_name, email=submitted_email, subject=submitted_subject, message=submitted_message) #not required to submit date as default is current date time

        details.save()  #commit
        print(submitted_name,submitted_email,submitted_subject,submitted_message)

    return redirect(index) # after submit go back to index page of client
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
