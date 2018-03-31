# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
# Create your views here.
def signout(request):
	try:
		request.session.pop("user",None)
	except Exception as err:
		msg="issue in logout: %s"%err.message
	return redirect("/signin/")

def customer(request):
	if request.session.get("user"):
		return render(request,"customer.html")
	else:
		return redirect("/signin/")
def signin(request):
	msg=""
	if request.method=="POST":
		form = UserForm(request.POST)
		if form.is_valid():
			try:
				data = form.cleaned_data
				user = authenticate(**data)
				if user:
					request.session['user']=user.username
					msg="success: %s welcom"%user.username
				else:
					msg="login failed"
			except Exception as err:
				msg=err.message	
	else:
		form = UserForm()
	return render(request,"signin.html",{"form":form,"msg":msg})

def signup(request):
	msg=""
	if request.method=="POST":
		form = UserForm(request.POST)
		if form.is_valid():
			try:
				data = form.cleaned_data
				data['password']= make_password(data['password'])
				user = User(**data)
				user.save()
				msg="success"
			except Exception as err:
				msg=err.message
	else:
		form = UserForm()
	return render(request,"signup.html",{"form":form,"msg":msg})
