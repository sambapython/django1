from django import forms
from models import Customer
from validators import validate_phone
# two kinds of forms: Normal forms, forms.Form and model forms, forms.ModelForm

class CustForm(forms.Form):
	# forms reduces the template code
	# can do validation
	first_name=forms.CharField(max_length=250)
	last_name=forms.CharField(max_length=250, required=False)
	address=forms.CharField(required=False)
	pic=forms.FileField()
	phonenumber=forms.CharField(max_length=12, 
		validators=[validate_phone])
	emailaddress=forms.EmailField()
	date = forms.DateField(required=False)

#class CustProductForm(form.Form):


class CustModelForm(forms.ModelForm):
	class Meta:
		model=Customer
		fields = ["first_name","last_name","address","pic",
		"phonenumber","emailaddress","date"]




