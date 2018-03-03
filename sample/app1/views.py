# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import Instructor
def instructor(request):
	data = Instructor.objects.all()
	return render(request,"list_instructor.html",{"data":data})
def delete_instructor(request, i_id):
	msg=""
	data=""
	try:
		data= Instructor.objects.get(id=i_id)
	except Exception as err:
		msg=err
	if request.method=="POST":
		flag = request.POST.get("yesno")
		if flag=="yes":
			data.delete()
			msg="deleted successfully"
			data=""
		else:
			msg="Changed your mind"
	return render(request,"delete_instructor.html",{"inst_data":data,"msg":msg})

def index(request):
	return render(request,"index.html")
def update_instructor(request, instructor_pk):
	msg=""
	if request.method=="POST":
		try:
			inst= Instructor.objects.get(id=instructor_pk)
			inst.name=request.POST.get("name")
			inst.email=request.POST.get("email")
			inst.mobile=request.POST.get("cell")
			inst.info=request.POST.get("extratext")
			inst.save()
			msg="record %s updated successfully" %instructor_pk
		except Exception as err:
			msg=err.message


	#print instructor_pk
	data=""
	try:
		data= Instructor.objects.get(id=instructor_pk)
	except Exception as err:
		msg=err.message
	#print data.name
	return render(request,"update_instructor.html",{"inst_data":data,"msg":msg})

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
		#return render(request,"create_instructor.html",{"message":msg})
		#data = Instructor.objects.all()
		#return render(request,"list_instructor.html",{"msg":msg,"data":data})
		return redirect("/instructor/")
	else:

		return render(request,"create_instructor.html")


