# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import Product

# Create your views here.
def home(request, page_number=""):
	if request.method=="POST":
		page_number=request.POST.get('page_number')
	if not page_number:
		page_number=1
	else:
		page_number = int(page_number)
	total_products=Product.objects.all().count()
	pages=range(0,total_products/100)
	products = Product.objects.all()[(page_number-1)*100:page_number*100]
	cols=[]
	data = map(lambda x: x.__dict__,products)
	map(lambda x:x.pop('_state'),data)
	if data:
		cols=data[0].keys()
	return render(request,"home.html",
		{"products":data,"cols":cols,"pages":pages,"page_number":page_number})
