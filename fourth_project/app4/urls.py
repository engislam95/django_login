from django.conf.urls import url
from app4 import views 
from django.urls import path 

app_name = 'app4'

urlpatterns = [
	path('alter/',views.alter,name='alter'),
	path('other/',views.other,name='other'),

]

