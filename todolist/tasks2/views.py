# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def tasks2_view(request):
	return render(request,"tasks2/base.html")
