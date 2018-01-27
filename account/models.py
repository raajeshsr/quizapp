# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User
# Create your models here.
from django.db.models.signals import post_save

from quiz.models import Question

def get_first_question():
	from quiz.models import Question
	return Question.objects.all()[0].id

class UserProfile(models.Model):
	user =models.OneToOneField(User)
	mark=models.IntegerField(default=0)
	test_date = models.DateTimeField(auto_now_add=True)
	#test_completed = models.BooleanField(default=False)
	current_question = models.IntegerField(default=get_first_question)
	def __str__(self):
		return str(self.mark)

def create_user_profile(sender,**kargs):
	if kargs['created']:
		UserProfile.objects.create(user=kargs['instance'])

post_save.connect(create_user_profile,sender=User)


class UserChoice(models.Model):
	user=models.ForeignKey(User)
	question=models.ForeignKey(Question)
	choice_text=models.CharField(max_length=300)
	def __str__(self):
		return self.choice_text