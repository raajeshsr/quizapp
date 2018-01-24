# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render,redirect

from django.http import HttpResponse,HttpResponseRedirect

from .models import Question,Choice
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from account.models import Result
from django.contrib.auth import login,logout

questions=Question.objects.all() 

q=questions[0]
i=q.id	

length=Question.objects.count()
q=questions[length-1]
last_question=q.id
print last_question
	
def getQuestion():
	global i
	try:
		q=Question.objects.get(pk=i)
	except Question.DoesNotExist:
		i+=1
		q=getQuestion()
		return q	
	else:
		i+=1
		return q		
	
		

def isLast():
	global i
	global last_question
	if i>last_question:
		return True
	else: 
		return False	

@login_required(login_url="/account/login/")  
def index(request):
	user=request.user
	obj,created = Result.objects.get_or_create(user=user)
	print isLast()
	if isLast():
		mark=Result.objects.get(user=user).mark
		return render(request,'quiz/result.html',{'mark':mark})
	else:	
		q=getQuestion()
		return render(request,'quiz/index.html',{'q':q})


@login_required(login_url="/account/login/")  
def validate(request,pk):
	#global length
	pk=int(pk)	
	q=Question.objects.get(pk=pk)
	c= request.GET['choice']
	ch=q.choice_set.get(choice_text=c)
	
	if ch.correct_choice:
		user=request.user
		r=Result.objects.get(user=user)
		r.mark+=1
		r.save()
	
	return redirect('quiz:index')	
