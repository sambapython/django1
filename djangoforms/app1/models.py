# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from validators import validate_phone

# Create your models here.
# four kinds of models
'''
1. Normal models
2. absract models
3. proxy models
4. inherit models
'''
class Product(models.Model):
	#normal model
	name=models.CharField(max_length=250)
	cost_price=models.IntegerField()
	discount = models.IntegerField()
	del_charges = models.IntegerField()
	
	@property
	def sale_price(self):
		return self.cost_price+self.del_charges-self.discount

class PersonAbstract(models.Model):
	# abstract model, Django not creates table for it.
	# can use this model as a parent model, so that no 
	# need to mention the fields in the child model
	#. To reduce the redundancy in columns

	first_name=models.CharField(max_length=250)
	last_name=models.CharField(max_length=250, blank=True, null=True)
	address=models.TextField(blank=True, null=True)
	pic=models.FileField(blank=True, null=True)
	date = models.DateField(blank=True, null=True)

	@property
	def full_name(self):
		# this will act as a column, but this is not stored in DB.
		# when ever you want to display, it will call this method automatically.
		return "%s, %s"%(self.first_name, self.last_name)
	class Meta:
		abstract=True

class Customer(PersonAbstract):
	#normal model
	phonenumber=models.CharField(max_length=12, 
		validators=[validate_phone])
	emailaddress=models.EmailField(unique=True)

class School(models.Model):
	#normal model
	name=models.CharField(max_length=250)

class Student(PersonAbstract):
	#normal model
	school=models.ForeignKey(School)



