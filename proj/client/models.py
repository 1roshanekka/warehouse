from django.db import models
import datetime

# Create your models here.

from django.db import models

class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField()

    # date = models.DateField(auto_now_add=True) #automatic
    date = models.DateField(default=datetime.date.today)
    def __str__(self):
        return self.name
