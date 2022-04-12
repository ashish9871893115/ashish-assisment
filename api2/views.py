from tokenize import Name
from django.views import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.db import models
from api2 import forms
from api2 import models

def register(request):
    if request.method == 'POST':
        user_creation_form = UserCreationForm(request.POST)
        if user_creation_form.is_valid():
            print('valid')
            user_creation_form.save()
            return redirect('/login/')
        else:
            user_creation_form = UserCreationForm()
            print('invalid')
            return render(request, 'signup.html', {'form': user_creation_form})
    else:
        user_creation_form = UserCreationForm()
        return render(request, 'signup.html', {'form': user_creation_form})

def log_in(request):
    if request.method=='POST':
        auth_form = AuthenticationForm(request=request, data=request.POST)
        if auth_form.is_valid():
            uname = auth_form.cleaned_data['username']
            upass = auth_form.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return redirect('/')
        else:
            return render(request,'login.html',{'auth_form':auth_form}) 
    else:
        auth_form = AuthenticationForm()
        return render(request,'login.html',{'auth_form':auth_form})
        

def log_out(request):
    logout(request)
    return redirect('homepage')


def homepage(request):
    return render(request,'homepage.html')

def addbook_view(request):
    form1=forms.BookForm()
    if request.method=='POST':
        form1=forms.BookForm(request.POST)
        if form1.is_valid():
            user=form1.save()
            return redirect('/viewbook/')
    return render(request,'addbook.html',{'form1':form1})

def viewbook_view(request):
    books=models.Book.objects.all()
    return render(request,'viewbook.html',{'books':books})

def delete(request,id):
        print('record deleted inti')
        records=models.Book.objects.get(id=id)
        records.delete()
        print('record deleted')
        return redirect('/viewbook/')

    