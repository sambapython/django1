# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Room(models.Model):
	noofbeds_choices = [('1',"Single bedroom"),
	('2',"Double bedroom"),
	('3',"Triple bedroom"),]
	types = [('ac', "AC ROOM"),
			('nac', "NON AC ROOM")]
	name=models.CharField(max_length=250)
	cost=models.IntegerField(max_length=250)
	noofbeds=models.CharField(choices=noofbeds_choices,
		max_length=2)
	type=models.CharField(choices=types, max_length=250)
