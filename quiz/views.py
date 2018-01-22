# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render,redirect

from django.http import HttpResponse,HttpResponseRedirect

from .models import Question,Choice
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
length=Question.objects.count()

global mark
	
@login_required(login_url="/account/login/")  
def index(request):
	global mark
	mark=0
	q=Question.objects.all() 
	q=q[0]
	pk=q.id
	return render(request,'quiz/index.html',{'q':q,'pk':pk})	

@login_required(login_url="/account/login/")  	
def disp(request,pk):
	pk=int(pk)
	pk+=1
	q=Question.objects.get(pk=pk)
	pk=q.id
	return render(request,'quiz/disp.html',{'q':q,'pk':pk})

@login_required(login_url="/account/login/")  
def validate(request,pk):
	global length
	global mark
	pk=int(pk)	
	q=Question.objects.get(pk=pk)
	c= request.GET['choice']
	ch=q.choice_set.get(choice_text=c)
	if ch.correct_choice:
		mark+=1
	if pk==length:
		user=request.user
		user.result_set.create(mark=mark)
		mark=str(mark)
		return render(request,'quiz/result.html',{'mark':mark})
	else:
		return redirect('quiz:disp',pk=pk)	
	
