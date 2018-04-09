# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import CreateView
from models import Customer
from django.forms.widgets import DateInput

# Create your views here.
'''
def index(request):
	return render(request,"app1/index.html")
'''

class CustomerCreateView(CreateView):
	model=Customer
	fields=["name","age","dob","created","cust_type"]
	success_url="/customer/"
	def get_form(self):
		form = CreateView.get_form(self)
		form.fields['dob'].widget=DateInput()
		return form
