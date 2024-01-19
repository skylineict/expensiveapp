from django.forms import fields, widgets
from .models import Register
from django import forms


class Signupform(forms.ModelForm):
    uplaod_img = forms.CharField(widget=forms.FileInput(
        attrs={"class": "form-control", 'type': 'file', 'id': 'formFile'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': "form-control", "type": " email",
                                                           "id": "emailinput", 'placeholder': 'emaill Address'

                                                           }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": 'form-control', "type": "text", "id": 'usernameinput', "placeholder": 'username'
    }))

    full_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', "type": "text", "id": 'fullnameinput', "placeholder": 'full name'
    }))

    class Meta:
        model = Register
        fields = ['uplaod_img', 'email', 'username', "full_name"]
