from django import forms
from models import OwnUser
from django.contrib.auth.models import User
class SignupForm(forms.Form):
	name = forms.CharField(max_length=100)
	username = forms.CharField(max_length=100)
	password = forms.CharField(max_length=100)
	#username = forms.CharField(widget=forms.Textarea)
	email = forms.EmailField()
	phone = forms.CharField(max_length=100)

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email","password"]

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]
        
class OwnUserForm(forms.ModelForm):
    class Meta:
        model = OwnUser
        fields = ["role1","name","phone"]

