# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from forms import CustForm, CustModelForm
from models import Customer

# Create your views here.
def create_customer(request):
	errors=""
	msg=""
	if request.method=="POST":
		try:
			cust_data =CustForm(request.POST,request.FILES) #  CustModelForm(request.POST,request.FILES)
			#import pdb; pdb.set_trace()
			if cust_data.is_valid():
				data = cust_data.cleaned_data
				cust_i = Customer(**data)
				cust_i.save()
				msg="customer created successfully!"
			else:
				errors = cust_data._errors
		except Exception as err:
			errors = err.message
	form = CustForm()
	#form2=CustForm()
	return render(request,"create_cust.html",
		{"form":form,
		#"form2":form2,
		"errors":errors,
		"msg":msg})
