# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_save
statuses = [("draft","draft"),("inprogress","inprogress"),("completed","completed")]

# Create your models here.
# class Company(models.Model):
# 	name = models.CharField(max_length=250)
# 	address = models.TextField()

# 	def __str__(self):
# 		return self.name

class Language(models.Model):
	name = models.CharField(max_length=500)
	def __str__(self):
		return self.name

class Job(models.Model):
	name = models.CharField(max_length=500)
	languages = models.ManyToManyField(Language)
	moreinfo = models.TextField()
	#createdby = models.ForeignKey(OwnUser)
	createddate = models.DateTimeField(auto_now=True)
	#company = models.ForeignKey(Company, blank=True, null=True)
	status = models.CharField(choices=statuses, max_length=250, default="draft") 
	def __str__(self):
		return self.name

class OwnUser(models.Model):
	user = models.OneToOneField(User)
	types_choices = [('aspirant', "aspirant"), ("recruiter", "recruiter")]
	name = models.CharField(max_length=250)
	phone = models.CharField(max_length=250)
   	role1 = models.CharField(choices=types_choices, max_length=30)
   	#company = models.ForeignKey(Company, blank=True, null=True)
   	applied_jobs = models.ManyToManyField(Job, blank=True, null=True)
	def __unicode__(self):
			return "%s"%(self.name)
	

class Recruitment(models.Model):
	
	name = models.CharField(max_length=250)
	jobs = models.ManyToManyField(Job)
	#company = models.ForeignKey(Company)
	createdby = models.ForeignKey(User)
	createddate = models.DateTimeField(auto_now=True)
	status = models.CharField(choices=statuses, max_length=250, default="draft")
	aspirants = models.ManyToManyField(OwnUser, blank=True, null=True)
	startdate = models.DateField(blank=True)
	enddate = models.DateField(blank=True)
	
	def __str__(self):
		return self.name

