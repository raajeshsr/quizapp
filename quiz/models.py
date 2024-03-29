# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User


# Create your models here.
class Question(models.Model):
	question_text = models.CharField(max_length=200)
	

	def __str__(self):
		return self.question_text
	
        


class Choice(models.Model):
	question = models.ForeignKey(Question,on_delete=models.CASCADE)
	choice_text=models.CharField(max_length=300)
	correct_choice = models.BooleanField(default=False)
	def __str__(self):
		return self.choice_text
		

class userSelections(models.Model):
	user=models.ForeignKey(User)
	question=models.ForeignKey(Question)
	selected = models.BooleanField(default=False)
	def __str__(self):
		return str(self.user)+" "+str(self.question)+" "+str(self.selected)