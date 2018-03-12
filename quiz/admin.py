# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from quiz.models import Question,Choice,userSelections
# Register your models here.

admin.site.register(Question)

admin.site.register(Choice)

admin.site.register(userSelections)
