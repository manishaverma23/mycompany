from django.shortcuts import render,HttpResponse,redirect
from .models import Contact, Quote,Service,Portfolio
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from . forms import ServiceUpdateForm,PortfolioUpdateForm



def index(request):
    info= Service.objects.all()
    data= Portfolio.objects.all()
    if request.method=='POST':
        email=request.POST['email']
        name=request.POST['name']
        mobile=request.POST['mobile']
        quote=Quote(email=email,name=name,mobile=mobile)
        quote.save()
    return render(request,'index.html',{'info':info,'data':data})

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
    # if request.method=='POST':
    #     email=request.POST['email']
    #     name=request.POST['name']
    #     mobile=request.POST['mobile']
    #     quote=Quote(email=email,name=name,mobile=mobile)
    #     quote.save()
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


def admin_contacts(request):
    contacts=Contact.objects.all()
    return render(request,'admin_contacts.html',{'contacts':contacts})

def quotations(request):
    quotations=Quote.objects.all()

    return render(request,'quotations.html',{'quotations':quotations})

def delete_contacts():
    d=Contact.objects.all(getid=id)
    d.delete()
    return redirect('admin_contacts')

def delete_quotations():
    d=Quote.objects.all(getid=id)
    d.delete()
    return redirect('quotations')

def services(request):
    if request.method=='POST':
        file=request.FILES['file']
        title=request.POST['title']
        description=request.POST['description']
        service=Service(file=file,title=title,description=description)
        service.save()
    return render(request,'services.html')

def watch_services(request):
    services=Service.objects.all()
    return render(request,'view_services.html',{'services':services})

def updateservice(request,id):
    u=Service.objects.get(id=id)
    form=ServiceUpdateForm(request.POST or None,request.FILES or None,instance=u)
    if form.is_valid():
        form.save()
        return redirect('watch_services')
    return render(request,'serviceupdate.html',{'u':u,'form':form})

def delete_view_service():
    s=Service.objects.all(getid=id)
    s.delete()
    return redirect('view_services')

def add_portfolio(request):
    if request.method=='POST':
        file=request.FILES['photo']
        text=request.POST['name']
        portfolio=Portfolio(file=file,text=text)
        portfolio.save()
    return render(request,'add_portfolio.html')

def view_portfolio(request):
    vport=Portfolio.objects.all()
    return render(request,'view_portfolio.html',{'vport':vport})

def updateportfolio(request,id):
    o=Portfolio.objects.get(id=id)
    pform=PortfolioUpdateForm(request.POST or None,request.FILES or None,instance=o)
    if pform.is_valid():
        pform.save()
        return redirect('view_portfolio')
    return render(request,'portfolioupdate.html',{'o':o,'pform':pform})

def delete_portfolio():
    z=Portfolio.objects.all(getid=id)
    z.delete()
    return redirect('view_portfolio')



