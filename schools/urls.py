from django.conf.urls import patterns, url
from schools import views

urlpatterns = patterns('', 
	url(r'^$', views.Intro.as_view(), name='FirstPage'),
)