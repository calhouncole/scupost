from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.views.generic.base import View
from classifieds.models import Classifieds
from users.models import Users
from schools.models import Schools
from django.shortcuts import render
from django.template import RequestContext, loader





#THE BELOW VARIABLES ARE ALL THE CATEGORIES THAT WILL BE DISPLAYED IN THE LISTINGS
For_Sale = ["Barter", "Bikes", "Computer", "Electronics", "Free", "Furniture", "Games", "General", "Household", "Media", "Music", "Sporting", "Textbooks", "Tickets", "Tools", "Wanted"]
personals = ['Friendship', 'General', 'Romance']
housing = ["Apts/Housing", "Roommates", "Rooms/Shared", "Sublets/Temporary", "Wanted"]
on_campus_jobs = ["Admin", "General", "Research", "Tutoring"] 
community = ["Activities", "Classes", "General", "Lost+Found", "Rideshare", "Volunteers"]

total_vars = ["", "Barter", "Bikes", "Computer", "Electronics", "Free", "Furniture", "Games", "Household", "Media", "Music", "Sporting", 
"Textbooks", "Tickets", "Tools", "Wanted", 'Friendship', 'Romance', "Apts/Housing", "Roommates", "Rooms/Shared", "Sublets/Temporary",
"Admin", "General", "Research", "Tutoring", "Activities", "Classes", "Lost+Found", "Rideshare", "Volunteers"]
total_vars = sorted(total_vars)

#THE FUNCTION: LISTINGS, RENDERS THE LISTINGS TEMPLATE, PASSISNG IN THE CATEGORIES AS VARIABLES
def listings(request):
	usr_id = request.session['id']
	context = {'For_Sale' : For_Sale, 'personals' : personals, 'housing' : housing, 'on_campus_jobs' : on_campus_jobs, 'community' : community, 'id' : usr_id}
	return render(request, 'classifieds/listings.html', context)

#THIS FUNCTION TAKES THE CATEGORY VARIABLE AND RENDERS ALL OF THOSE IN THE DATABSE ASSOCIATED WITH THAT CATEGORY	

def detail(request, types):
	latest_list = Classifieds.objects.filter(category = types)
	output = []

	for each_listing in latest_list:
		output.append(each_listing)


	context = {'output': output}
	return render(request, 'classifieds/detail.html', context)

def specific(request, specific_id):
	object_database = Classifieds.objects.get(pk=specific_id)
	if object_database:
		spec_user = object_database.user.email
		spec_title = object_database.title
		spec_description = object_database.description
		context = {'spec_title': spec_title, 'spec_description': spec_description, 'spec_user': spec_user}
		return render(request, 'classifieds/specific.html', context)
		
	else:
		return HttpResponse("Sorry! The posting you are looking for does not exist.")

#RENDERS THE POSTING PAGE, GETS THE USERS INFO AND INPUTS IT TO THE DATABASE
class Post(View):
	def get(self, request):
		context = {'total_vars': total_vars}
		return render(request, 'classifieds/post.html', context)
	def post(self, request):
		title = request.POST.get('title')
		price = request.POST.get('price')
		description = request.POST.get('description')
		category = request.POST.get('category')
		new_classified = Classifieds(title = title, category = category, description = description,
				user = Users.objects.get(pk = request.session['id']), school = Schools.objects.get(pk=1))
		new_classified.save()
		return HttpResponseRedirect('/classifieds/')
