from django.shortcuts import render,HttpResponse
from .models import Contact, Quote



def index(request):
    if request.method=='POST':
        email=request.POST['email']
        name=request.POST['name']
        mobile=request.POST['mobile']
        quote=Quote(email=email,name=name,mobile=mobile)
        quote.save()
    return render(request,'index.html')

def about(request):
    if request.method=='POST':
        email=request.POST['email']
        name=request.POST['name']
        mobile=request.POST['mobile']
        quote=Quote(email=email,name=name,mobile=mobile)
        quote.save()
    return render(request,'about.html')

def contact(request):
    if request.method=='POST':
        email=request.POST['email']
        name=request.POST['name']
        message=request.POST['message']
        contact=Contact(email=email,name=name,message=message)
        contact.save()
    if request.method=='POST':
        email=request.POST['email']
        name=request.POST['name']
        mobile=request.POST['mobile']
        quote=Quote(email=email,name=name,mobile=mobile)
        quote.save()
    return render(request,'contact.html')