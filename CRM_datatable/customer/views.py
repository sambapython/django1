# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import Customer
from django.contrib import messages


# Create your views here.
def get_data(model_name):
	total_data = []
	columns = []
	total_data = model_name.objects.all()
	if total_data:
		columns = total_data[0].__dict__.keys()
		columns.remove("_state") if "_state" in columns else ""
		data = map(lambda x:x.__dict__, total_data)
		map(lambda x:x.pop("_state",None),data)
	return {"data":data,"columns":columns}


def index(request):
	return render(request,"customers/index.html")

def customer_view(request):
	return render(request,"customers/customer_index.html",get_data(Customer))

def create_customer(request):
	msg=""
	if request.method=="POST":
		try:
			name=request.POST.get("cust_name")
			email=request.POST.get("cust_email")
			phone=request.POST.get("cust_phone")
			customer = Customer(name=name, email=email, phone=phone)
			customer.save()
			print 1/0
			messages.success(request, "Customer created successfully")
			return redirect("/customer/")
		except Exception as err:
			messages.error(request, err.message)
	return render(request,"customers/create_customer.html")