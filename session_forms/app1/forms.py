from django import forms

class UserForm(forms.Form):
	username=forms.CharField(max_length=250)
	password=forms.CharField(max_length=250,widget=forms.PasswordInput)
