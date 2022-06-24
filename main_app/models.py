from django.core.checks import messages
from django.db import models

# Create your models here.


class Request(models.Model):
    """Contact information of the client"""
    first_name = models.CharField(max_length=30)
    e_mail = models.EmailField(max_length=200)
    messages = models.TextField(max_length=500)
    date_info = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.first_name
