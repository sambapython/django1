# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#def users_view(request):
#	return "some value"
def users_view(request):
	return HttpResponse("Hello Firefox. I am hitting you from users_view")
def users_view1(request):
	#return HttpResponse("Hello Firefox. I am hitting you from users_view1")
	#return "Hello Firefox. I am hitting you from users_view1"
	return HttpResponse("Hello Firefox. I am hitting you from users_view1")

def users_view2(request):
	#return HttpResponse("Hello Firefox. I am hitting you from users_view1")
	#return "Hello Firefox. I am hitting you from users_view1"
	return HttpResponse("Hello Firefox. I am hitting you from users_view2")
def url_fun(request):

	#return HttpResponse("sample response")

	#return HttpResponse("<h1>sample response</h1>")
	#data = open("/home/khyaathi-python/pythonexamples/djang0-batch1/app3.html").read()
	#return HttpResponse(data)
    return render(request,"base.html")

