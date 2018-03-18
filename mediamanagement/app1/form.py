from django import forms

class CustomerForm(forms.Form):
	name=forms.CharField(max_length=250, lable="Customer Name")
	profile_name = forms.CharField(max_length=250, lable="Customer profile pic")