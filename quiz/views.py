from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
<<<<<<< HEAD
from .models import Question,Choice
from account.models import UserProfile
from account.models import UserChoice

=======
from account.models import Result
from django.contrib.auth import login,logout
>>>>>>> 1f00947ae9f177659d47e592dbe34bcb5b25936f

questions=Question.objects.all() 
length=Question.objects.count()

<<<<<<< HEAD

first_question=questions[0].id
last_question=questions[length-1].id


@login_required(login_url="/")  
def previousQuestion(request,pk):
	current_user=request.user
	user=UserProfile.objects.get(user=current_user)
	count=Question.objects.filter(pk__lt=pk).count()
	user.current_question=Question.objects.filter(pk__lt=pk)[count-1].id
	user.save()
	
	#getting previous question option
	question=Question.objects.get(pk=user.current_question)
	saved_choice=UserChoice.objects.get(user=current_user,question=question)
=======
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
>>>>>>> 1f00947ae9f177659d47e592dbe34bcb5b25936f
	
	
	if question.choice_set.get(choice_text=saved_choice).correct_choice:
		decrementMark(user)

	return render(request,'quiz/index.html',{'question':question,'first_question':first_question,'last_question':last_question,'saved_choice':saved_choice.choice_text})


def isLast(pk):
	pk=int(pk)
	if pk==last_question:
		return True
	else: 
		return False	

<<<<<<< HEAD

@login_required(login_url="/")  
def index(request,pk):

	question=Question.objects.get(pk=pk)	
	return render(request,'quiz/index.html',{'question':question,'first_question':first_question,'last_question':last_question})


@login_required(login_url="/")  
def nextQuestion(request,pk):
	
	question=Question.objects.get(pk=pk)
	
	selected_choice= request.GET['choice']
	
	current_user=request.user

	choice=question.choice_set.get(choice_text=selected_choice)
	
	user=UserProfile.objects.get(user=current_user)
	
	saveChoice(current_user,question,selected_choice)


	if choice.correct_choice:
		
		incrementMark(user)

	if isLast(pk):	
		
		deactivateUser(current_user)

		return render(request,'quiz/result.html',{'mark':user.mark})
	
	else:	
	
		user.current_question=Question.objects.filter(pk__gt=pk)[0].id
	
		user.save()	
	
		return redirect('quiz:index',pk=user.current_question)	


def saveChoice(current_user,question,selected_choice):
	try:
		saved_choice=UserChoice.objects.get(user=current_user,question=question)

	except UserChoice.DoesNotExist:	

		UserChoice.objects.create(user=current_user,question=question,choice_text=selected_choice)

	else:

		saved_choice.choice_text=selected_choice
		
		saved_choice.save()	

def incrementMark(user):
	user.mark+=1
	user.save()


def decrementMark(user):
	user.mark-=1
	user.save()

def deactivateUser(current_user):
	current_user.is_active=False
	current_user.save()
=======
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
>>>>>>> 1f00947ae9f177659d47e592dbe34bcb5b25936f
