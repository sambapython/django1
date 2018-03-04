# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Instructor(models.Model):
	name = models.CharField(max_length=250)
	mobile = models.IntegerField()
	email = models.EmailField()
	info = models.TextField()

class Course(models.Model):
	name=models.CharField(max_length=250)
	duration = models.IntegerField()
	fee = models.IntegerField()
	starttime = models.CharField(max_length=50)
	endtime = models.CharField(max_length=50)
	enddate = models.DateField()
	startdate = models.DateField()
	instructor = models.ForeignKey(Instructor)
	status = models.CharField(choices=[
		("draft","DRAFT"),
		("inprogress","INPROGRESS"),
		("complete","COMPLETE")], max_length=20)
	info = models.TextField()


