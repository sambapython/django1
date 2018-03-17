# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Company(models.Model):
	name = models.CharField(max_length=250, unique=True)
	address = models.CharField(max_length=250, null=True, blank=True, 
		default="ameerpet")

	def __str__(self):
		return "%s,%s"%(self.name, self.address)

class Customer(models.Model):
	name=models.CharField(max_length=250)
	company = models.ForeignKey(Company)

	def __str__(self):
		return "%s,%s"%(self.name,self.company.name)
class Product(models.Model):
	name=models.CharField(max_length=250)
	sales_price=models.IntegerField()
	color=models.CharField(max_length=10, blank=True, null=True)
	def __str__(self):
		return self.name

class SalesOrder(models.Model):
	statuses = [('d',"DRAFT"),('i',"INPROGRESS"),("c","COMPLETE")]
	desc=models.TextField(default="zxffgfd")
	customer=models.ForeignKey(Customer, on_delete=models.PROTECT)
	products=models.ManyToManyField(Product)
	status = models.CharField(max_length=1, choices=statuses,
		default="d")
	date = models.DateField(auto_now=True) 
	completed_date=models.DateTimeField(null=True, blank=True)
	delivered = models.BooleanField(default=False)

	def __str__(self):
		return "%s, %s, %s"%(self.id,self.desc, self.get_status_display())

class Withprimarykey(models.Model):
	name=models.CharField(primary_key=True,max_length=250)
