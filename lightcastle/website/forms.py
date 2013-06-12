from django import forms
from django.shortcuts import redirect
from django.views.generic import FormView

class ContactForm(forms.Form):

    name = forms.CharField(required=True, initial="BILL")
    email = forms.CharField(required=True)
    message = forms.CharField(required=True, max_length=500)

