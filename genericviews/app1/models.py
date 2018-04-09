# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Customer(models.Model):
	customer_types=[
	("g","GOLD"),
	("s","silver"),
	("n","NORMAL"),
	("b","BRONZE"),
	]
	name=models.CharField(max_length=250)
	age=models.IntegerField()
	dob=models.DateField()
	created = models.DateTimeField()
	cust_type=models.CharField(choices=customer_types, max_length=2)

	def __str__(self):
		return "%s-%s-%s"%(self.name, self.age, self.get_cust_type_display())
