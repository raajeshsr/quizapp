
from django.conf.urls import url,include
from django.contrib import admin
from . import views
app_name="quiz"
urlpatterns = [
    url(r'^(?P<pk>[0-9]+)$',views.index,name="index"),
    url(r'^next/(?P<pk>[0-9]+)$',views.nextQuestion,name="nextQuestion"),
    url(r'^previous/(?P<pk>[0-9]+)$',views.previousQuestion,name="previousQuestion"),
    
    
]
