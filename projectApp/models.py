from django.db import models

class Contact(models.Model):
    email= models.CharField(max_length=30)
    name= models.CharField(max_length=30)
    message=models.TextField(max_length=50)

class Quote(models.Model):
    email=models.CharField(max_length=30)
    name=models.CharField(max_length=30)
    mobile=models.CharField(max_length=10)

class Service(models.Model):
    file=models.FileField(upload_to="images/")
    title=models.CharField(max_length=30)
    description=models.TextField(max_length=50)

class Portfolio(models.Model):
    file=models.FileField(upload_to="images/")
    text=models.CharField(max_length=30)

    def __str__(self):
        return self.text


    