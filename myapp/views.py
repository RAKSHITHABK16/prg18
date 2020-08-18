from django.shortcuts import render,redirect
from django.http import HttpResponse


# Create your views here.

from myapp import forms

def builtinforms(request):
    form=forms.SampleForm()
    return render(request,'builtin.html',{'form':form})


# forms is a file or a library
# in forms Form is a class so we inherit from forms.Form