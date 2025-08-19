from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=15)
    email=models.EmailField()
    content=models.TextField(max_length=500)
