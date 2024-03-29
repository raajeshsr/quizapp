from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .models import Question,Choice,userSelections
from account.models import UserProfile
from account.models import UserChoice


questions=Question.objects.all() 
length=Question.objects.count()


first_question=questions[0].id
last_question=questions[length-1].id


@login_required(login_url="/")  
def index(request,pk):
	current_user=request.user
	username=current_user.username
	
	#initializing userselection model
	for question in questions:
		userSelections.objects.get_or_create(user=current_user,question=question)



	#selections of current user	
	selections=userSelections.objects.filter(user=current_user)



	if(request.method=='POST'):		

		if(request.POST['nav']=='next'):
			pk=nextQuestion(request,pk)

		if(request.POST['nav']=='previous'):
			pk,saved_choice=previousQuestion(request,pk)
			question=Question.objects.get(pk=pk)	
			return render(request,'quiz/index.html',{'selections':selections,'question':question,'first_question':first_question,'last_question':last_question,'saved_choice':saved_choice,'username':username})

		if(request.POST['nav']=='submit'):
			mark=result(request,pk)
			return render(request,'quiz/result.html',{'mark':mark,'username':username})

	question=Question.objects.get(pk=pk)	
	return render(request,'quiz/index.html',{'selections':selections,'question':question,'first_question':first_question,'last_question':last_question,'username':username})

def previousQuestion(request,pk):
	current_user=request.user
	user=UserProfile.objects.get(user=current_user)

	#getting previous question no
	question_list=Question.objects.filter(pk__lt=pk)
	question_list_length=question_list.count()
	user.current_question=Question.objects.filter(pk__lt=pk)[question_list_length-1].id
	user.save()
	
	question=Question.objects.get(pk=user.current_question)
	
	saved_choice,created=UserChoice.objects.get_or_create(user=current_user,question=question)



	#reducing mark if previous ans is correct 
	try:
		previous_choice=question.choice_set.get(choice_text=saved_choice)
		if previous_choice.correct_choice:
			decrementMark(user)

	except Choice.DoesNotExist:
	
		pk=user.current_question
		
		#returns null to template
		saved_choice=saved_choice.choice_text	

		return pk,saved_choice

	markUnanswered(current_user,question)

	pk=user.current_question
	
	saved_choice=saved_choice.choice_text	

	return pk,saved_choice


def nextQuestion(request,pk):
	
	question=Question.objects.get(pk=pk)

	selected_choice= request.POST.get('choice',False)
	
	current_user=request.user
		
	user=UserProfile.objects.get(user=current_user)
				
	if selected_choice:

		userSelection=userSelections.objects.get(user=current_user,question=question)

		userSelection.selected=True
		userSelection.save()

		selectedChoice=question.choice_set.get(choice_text=selected_choice)
		
		saveChoice(current_user,question,selected_choice)

		validate(selectedChoice,user)
		
		
	user.current_question=Question.objects.filter(pk__gt=pk)[0].id
		
	user.save()		
		
	pk=user.current_question

	return pk

def result(request,pk):
	current_user=request.user

	selected_choice= request.POST.get('choice',False)

	user=UserProfile.objects.get(user=current_user)

	question=Question.objects.get(pk=pk)


	if selected_choice:
	
		markAnswered(current_user,question)

		selectedChoice=question.choice_set.get(choice_text=selected_choice)

		validate(selectedChoice,user)

		saveChoice(current_user,question,selected_choice)

	#deactivateUser(current_user)

	mark = user.mark

	return mark
	
def validate(selectedChoice,user):

	if selectedChoice.correct_choice:
		
		incrementMark(user)




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


def markAnswered(current_user,question):
	userSelection=userSelections.objects.get(user=current_user,question=question)
	userSelection.selected=True
	userSelection.save()

def markUnanswered(current_user,question):
	userSelection=userSelections.objects.get(user=current_user,question=question)
	userSelection.selected=False
	userSelection.save()
