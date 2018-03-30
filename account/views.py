# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from account.models import UserProfile
from django.contrib.auth import authenticate	
	
def signup_view(request):
	if(request.method=="POST"):
		form = UserCreationForm(request.POST)
		if form.is_valid():

			registered_user=form.save()
			user=UserProfile.objects.get(user=registered_user)
			user.college=request.POST['college']
			user.save()

			return redirect('account:login')
	else:	
		form = UserCreationForm()
	return render(request,'account/signup.html',{'form':form})

def login_view(request):
	if(request.method=='POST'):
		username =request.POST['username']	
		password = request.POST['password']
		user=authenticate(username=username,password=password)	

		if user is not None:
			if user.is_superuser:
				userProfile=UserProfile.objects.all().exclude(user__is_superuser='True').order_by('mark').reverse()
				return render(request,'quiz/marklist.html',{'userProfile':userProfile})	



			if user.is_active:
				current_question=UserProfile.objects.get(user=user).current_question	
				login(request,user)
				
				return redirect('quiz:index',pk=current_question)
			
		else:
			error_message="invalid username/password or you have taken test already"
		
		form = AuthenticationForm()
		return render(request,'account/login.html',{'form':form,'error_message':error_message})	
	
	else:
		form = AuthenticationForm()
		return render(request,'account/login.html',{'form':form})
	

def logout_view(request):
	logout(request)
	return redirect('account:login')
