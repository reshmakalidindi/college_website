

from django import forms
class SignUpForm(forms.Form):
    username=forms.CharField(labels="Name:")
    password=forms.CharFeild(labels="Password:")
    email=forms.EmailInput()