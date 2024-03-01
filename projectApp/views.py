from django.shortcuts import render,HttpResponse,redirect
from .models import Contact, Quote
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages



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


def admin_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('admin_dash')
        else:
            messages.error(request,'Invalid UserName Or Password')
            return redirect('admin_login')
    return render(request,'admin_login.html')

def admin_regi(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        admin=User.objects.create_user(username,email,password)
        admin.save()
        return redirect('admin_login')
    return render(request,'admin_regi.html')

def admin_dash(request):
    return render(request,'admin_dash.html')