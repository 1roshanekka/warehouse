from django import forms

class ContactForm(forms.Form):
    # Define your form fields here (e.g., name, email, subject, message)
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
