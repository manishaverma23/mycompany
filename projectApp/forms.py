from django import forms
from django.forms import Form,ModelForm
from  . models import Service,Portfolio

class ServiceUpdateForm(ModelForm):
    class Meta:
        model=Service
        fields=('file','title','description')
        
        widgets={
            'file':forms.FileInput(attrs={'class':'form-control w-100'}),
            'title':forms.TextInput(attrs={'class':'form-control w-100'}),
            'description':forms.TextInput(attrs={'class':'form-control w-100'})

        }

class PortfolioUpdateForm(ModelForm):
    class Meta:
        model=Portfolio
        fields=('file','text')

        widgets={
            'file':forms.FileInput(attrs={'class':'form-control w-100'}),
            'text':forms.TextInput(attrs={'class':'form-control w-100'})
        }