# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from forms import UserForm, OwnUserForm, LoginForm
from django.contrib import auth
from django.contrib.auth import authenticate
from models import OwnUser, Recruitment, Job
from django.db.models import Sum
from django_tables2 import tables

def changedrive(request, num=1):
	user_name = request.session['user']
	if user_name:
		drive = Recruitment.objects.get(pk=num)
		if drive.status == "draft":
			drive.status="inprogress"
		else:
			drive.status = "completed"
		drive.save()
		return redirect("/recruiterscreen/")
	else:
		return redirect("/login/")
def job_apply(request, num=1):
	user_name = request.session['user']
	if user_name:
		user_obj=OwnUser.objects.get(name=user_name)
		user_obj.applied_jobs.add(Job.objects.get(pk=num))
		user_obj.save()
		return redirect('/aspirantscreen/')
	else:
		return redirect("/login/")
def aspirantscreen(request):
	user_name = request.session['user']
	if user_name:
		jobs = Job.objects.filter(status__in=['draft','inprogress'])
		data = []
		user_obj = OwnUser.objects.get(name=user_name)
		if user_obj.applied_jobs:
			applied_jobs = [job.id for job in user_obj.applied_jobs.all()]
		for job in jobs:
			data.append({
				'name':job.name,
				'id': job.id,
				'createddate':"%s" % job.createddate,
				"status": job.status,
				"applied": job.id in applied_jobs
				})
		return render(request,'aspirantscreen.html',{"data":data})
	else:
		return redirect("/login/")

def recruiterscreen(request):
	user_name = request.session.get("user")
	if user_name:
		user_obj = OwnUser.objects.get(user__username=user_name)
		data = Recruitment.objects.all()
		result = []
		for row in data:
			jobs =  ",".join([job.name for job in row.jobs.all()])
			result.append({
				"id": row.id,
				"name": row.name,
				"status":row.status,
				"jobs": jobs,
				'createddate':"%s" % row.createddate,
				'count':30
				})
		return render(request, "recruiterscreen.html",{"data":result})
	else:
		return redirect("/login/")


def index(request):
	return render(request, "index.html",{'data':"data"})

def logout(request):
	request.session['user']=None
	return redirect("/index/")

def login(request):
	messages = []
	try:
		if request.method=="POST":
			user = LoginForm(request.POST)
			user = authenticate(username=request.POST['username'],password=request.POST['password'])
			if user:
				ownuser = OwnUser.objects.get(user=user)
				request.session['user']=ownuser.name
				messages.append("Login successfully")
				if ownuser.role1=="aspirant":
					return redirect("/aspirantscreen/")
				else:

					return redirect("/recruiterscreen/")
			else:
				messages.append("Login failed")
	except Exception as err:
			messages.append(err.message)
	return render(request, "login.html",{"form":LoginForm,
		"messages":messages})

def signup(request):
	messages = []
	try:
		if request.method=="POST":
			user_data = {}
			user_data.update({"username":request.POST.get("username"),
				"password": make_password(request.POST.get("password")),
				"email":request.POST.get("email"),
				 "is_staff":True,
				})
			user =   User(**user_data)
			ouform = OwnUserForm(data = request.POST)
			user.save()
			profile = ouform.save(commit = False)
			profile.user = user
			profile.save()
			messages.append("User created successfully")
	except Exception as err:
			messages.append(err.message)
	return render(request, "signup.html",{"uform":UserForm, "ouform":OwnUserForm,
		"messages":messages})
	
