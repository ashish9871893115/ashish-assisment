from django import forms
from django.contrib.auth.models import User
from api2 import models

class BookForm(forms.ModelForm):
    class Meta:
        model=models.Book
        fields="__all__"
