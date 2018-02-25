# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import Instructor

# Create your views here.
def create_instructor(request):
	if request.method=="POST":
		try:
			inst_obj = Instructor(name=request.POST.get("name"),
								email=request.POST.get("email"),
								mobile=request.POST.get("cell"),
								info=request.POST.get("extratext"))
			inst_obj.save()
			msg="successfully created instructor"
		except Exception as err:
			msg=err.message()
		return render(request,"create_instructor.html",{"message":msg})
	else:

		return render(request,"create_instructor.html")


