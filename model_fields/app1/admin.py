# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Company, Customer, Product, SalesOrder

# Register your models here.
admin.site.register(Company)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(SalesOrder)
