from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.views.generic.base import View
from classifieds.models import Classifieds
from users.models import Users
from schools.models import Schools
from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader
from django.contrib.formtools.wizard.views import SessionWizardView
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
from django.core.urlresolvers import reverse
from classifieds.models import Document
from classifieds.forms import DocumentForm






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
		spec_photo = object_database.photos
		context = {'spec_photo': spec_photo, 'spec_title': spec_title, 'spec_description': spec_description, 'spec_user': spec_user}
		return render(request, 'classifieds/specific.html', context)
		
	else:
		return HttpResponse("Sorry! The posting you are looking for does not exist.")

def post(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            new_classified = Classifieds(photos = request.FILES['docfile'], title = request.POST['title'], category = request.POST.get('category'), 
            				description = request.POST['description'], user = Users.objects.get(pk = request.session['id']), school = Schools.objects.get(pk=1))
            new_classified.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect('/classifieds')
    else:
        form = DocumentForm() # A empty, unbound form




    # Render list page with the documents and the form
    return render_to_response(
        'classifieds/list.html',
        {'form': form, 'total_vars': total_vars},
        context_instance=RequestContext(request)
)