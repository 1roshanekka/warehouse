from django.contrib import admin

# Register your models here.
from .models import ContactForm

class submittedForm(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(ContactForm, submittedForm)