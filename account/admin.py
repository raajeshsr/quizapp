# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Result
# Register your models here.

class ResultAdmin(admin.ModelAdmin):
	list_display=('mark','test_date')
	

	list_filter=['test_date'];


admin.site.register(Result,ResultAdmin)