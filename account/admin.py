# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import UserProfile
# Register your models here.
from .models import UserChoice
class UserProfileAdmin(admin.ModelAdmin):
	list_display=('mark','test_date')
	

	list_filter=['test_date'];


admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(UserChoice)