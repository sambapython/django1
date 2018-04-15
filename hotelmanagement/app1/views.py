# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from forms import RoomModelForm
from models import Room

# Create your views here.
def index(request):
	return render(request,"app1/home.html")

def rooms(request):
	return render(request, "app1/rooms.html")

def customers(request):
	return render(request, "app1/customers.html")

def reports_view(request):
	return render(request, "app1/reports.html")

def create_room(request):
	if request.method=="POST":
		form=RoomModelForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			room_inst=Room(**data)
			room_inst.save()

	form=RoomModelForm()
	return render(request, "app1/create_room.html",{"form":form})
