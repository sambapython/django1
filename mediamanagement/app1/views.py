# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from django.shortcuts import render
from models import Customer
from django.conf import settings

# Create your views here.
def customer(request):
	return render(request,"cust_index.html",{"data":Customer.objects.all()})
def create_customer_form(request):
	msg=""
	if request.method=="POST":
		pass
	else:
		pass

def create_customer(request):
	msg=""
	if request.method=="POST":
		try:
			customer = Customer(name=request.POST.get("name"))
			customer.save()
			cust_id = customer.id 
			media = request.FILES.get('profile')
			media_name=media.name 
			file_name = "%s_%s"%(cust_id,media_name)
			file_path=os.path.join(settings.MEDIA_ROOT,file_name)
			f=open(file_path,"wb")
			for chunk in media.chunks(): 
				f.write(chunk)
			f.close()
			customer.profile_name=file_name
			customer.save()
			msg="success"
		except Exception as err:
			msg=err.message
	return render(request,"create_customer.html",{"nsg":msg})
