# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# from validators import phone_validate

# Create your models here.

class Customer(models.Model):
	name=models.CharField(max_length=250)
	#phone=models.CharField(max_length=12, validators=[phone_validate])
	phone=models.CharField(max_length=12)
	email=models.EmailField()

