from django.db import models

class Contact(models.Model):
    email= models.CharField(max_length=30)
    name= models.CharField(max_length=30)
    message=models.TextField(max_length=50)

class Quote(models.Model):
    email=models.CharField(max_length=30)
    name=models.CharField(max_length=30)
    mobile=models.CharField(max_length=10)