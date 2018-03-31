# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from app1.models import Product

# Create your models here.
class MyProduct(Product):
	# inherit model
	# if you want add any columns, then go for inheri models.
	# this will create a table in database to store extrafileds
	color=models.CharField(max_length=30)


class ProductProxy(Product):
	# proxy model
	# if want to add only properites but don't want to add
	# the columns then go for proxy modles. Proxy model does not 
	# creates table in the database
	@property
	def discount_value(self):
		return self.cost_price*(self.discount/100.0)
	class Meta:
		proxy=True
