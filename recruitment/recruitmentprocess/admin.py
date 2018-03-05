# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from models import Language, Job, OwnUser, Recruitment
for i in [Language, Job, OwnUser, Recruitment]:
	admin.site.register(i)