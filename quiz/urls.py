
from django.conf.urls import url,include
from django.contrib import admin
from . import views
app_name="quiz"
urlpatterns = [
    url(r'^$',views.index,name="index"),
    url(r'^validate/(?P<pk>[0-9]+)$',views.validate,name="validate"),
    url(r'^disp/(?P<pk>[0-9]+)$',views.disp,name="disp"),
    
]
