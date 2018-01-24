# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User
# Create your models here.


class Result(models.Model):
	user =models.OneToOneField(User)
	mark=models.IntegerField(default=0)
	test_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.mark)
			