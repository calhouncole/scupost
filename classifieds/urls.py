from django.conf.urls import patterns, url
from classifieds import views


urlpatterns = patterns('', 
	url(r'^$', views.listings, name='Listings'),  #DIRECTS TO THE LISTINGS 
	url(r'^search/$', views.search, name = 'Search'),
	url(r'^post/$', views.post, name='Post'),
	url(r'^(?P<types>[a-zA-Z+/ ]+)/$', views.detail, name='Detail'), #ONCE A CATEGORY IS CLICKED IN LISTINGS PAGE, THIS SENDS THAT CATEGORY VARIABLE TO THE DETAIL VIEW 
	url(r'^(?P<specific_id>\d+)/$', views.specific, name='Specific'),
	
)