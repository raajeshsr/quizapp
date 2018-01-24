# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

from django.contrib.auth import login,logout

from django.contrib.auth.decorators import login_required

from braces.views import LoginRequiredMixin
  
	
	
def signup_view(request):
	if(request.method=="POST"):
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('account:login')
	else:	
		form = UserCreationForm()
	return render(request,'account/signup.html',{'form':form})

def login_view(request):
	if(request.method=='POST'):
		form=AuthenticationForm(data=request.POST)
		if form.is_valid():
			user=form.get_user()
			login(request,user)
			return redirect('quiz:index')
	else:
		form = AuthenticationForm()
	return render(request,'account/login.html',{'form':form})

def logout_view(request):
	logout(request)
	return render(request,'account/signup.html')



