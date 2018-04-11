# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class RequestTracker(models.Model):
	url=models.CharField(max_length=1000)
	createdatetime=models.DateTimeField(auto_now_add=True, blank=True)
	modifydatetime=models.DateTimeField(auto_now=True, blank=True)
	status_code=models.CharField(max_length=5, blank=True)

	def __str__(self):
		return "%s,%s,%s,%s"%(self.url, self.createdatetime,
			self.modifydatetime, self.status_code)
