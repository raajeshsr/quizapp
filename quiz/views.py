# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render,redirect

from django.http import HttpResponse,HttpResponseRedirect

from .models import Question,Choice
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from account.models import Result
from django.contrib.auth import login,logout
# Create your views here.
#print "hello"
#global mark

questions=Question.objects.all() 

q=questions[0]
i=q.id	
#print i

length=Question.objects.count()
q=questions[length-1]
last_question=q.id
print last_question

'''question = get_object_or_404(Questions, pk=id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'poll/detail.html', {
			'question': question,
			'error_message': "You didn't select a choice.",
			})'''
	
def getQuestion():
	global i
	try:
		q=Question.objects.get(pk=i)
	except Question.DoesNotExist:
		i+=1
		q=getQuestion()
		return q	
	else:
		#print i
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

	'''q=Question.objects.all() 
	q=q[0]
	pk=q.id
	user=request.user
	obj,created = Result.objects.get_or_create(user=user)
	if created:
		return render(request,'quiz/index.html',{'q':q,'pk':pk})
	else:
		logout(request)
		return HttpResponse("<p>you have already taken the quiz</p>")	

	return render(request,'quiz/index.html',{'q':q,'pk':pk})

	
@login_required(login_url="/account/login/")  	
def disp(request,pk):
	pk=int(pk)
	pk+=1
	q=Question.objects.get(pk=pk)
	pk=q.id
	return render(request,'quiz/disp.html',{'q':q,'pk':pk})

'''

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
		
	#if pk==length:
	#	mark=r.mark
	#	return render(request,'quiz/result.html',{'mark':mark})
	#else:
	return redirect('quiz:index')	
