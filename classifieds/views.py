from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.views.generic import View
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
from classifieds.forms import DocumentForm
from django.core.mail import send_mail
from django.utils import timezone






#THE BELOW VARIABLES ARE ALL THE CATEGORIES THAT WILL BE DISPLAYED IN THE LISTINGS
For_Sale = ["Barter", "Bikes", "Computer", "Electronics", "Free", "Furniture", "Games", "General", "Household", "Media", 
			"Music", "Sporting", "Textbooks", "Tickets", "Tools"]
personals = ['Friendship', 'General', 'Romance']
housing = ["Apts/Housing", "Roommates", "Rooms/Shared", "Sublets/Temporary"]
on_campus_jobs = ["Admin", "General", "Research", "Tutoring"] 
community = ["Activities", "Classes", "General", "Lost+Found", "Parties", "Rideshare", "Volunteers"]
Wanted = ["Wanted"]
total_vars = ["Barter", "Bikes", "Computer", "Electronics", "Free", "Furniture", "Games", "Household", "Media", "Music", 
				"Sporting", 
				"Textbooks", "Tickets", "Tools", "Wanted", 'Friendship', 'Romance', "Apts/Housing", "Roommates", 
				"Rooms/Shared", "Sublets/Temporary",
				"Admin", "General", "Research", "Tutoring", "Activities", "Classes", "Lost+Found", "Rideshare", 
				"Volunteers", "Parties"]
total_vars = sorted(total_vars)



# THE FUNCTION: LISTINGS, QUERIES THE DB FOR 10 RECENT POSTS, RENDERS THE LISTINGS TEMPLATE, PASSISNG IN THE CATEGORIES 
# AND RECENT POSTS AS VARIABLES
def listings(request):
	recent_posts = []
	recent_posts_temp = Classifieds.objects.order_by('-pub_date')[:10]
	for each in recent_posts_temp:
		recent_posts.append(each)

	context = {'recent_posts': recent_posts, 'Wanted': Wanted, 'For_Sale' : For_Sale, 'personals' : personals, 'housing' : housing, 
				'on_campus_jobs' : on_campus_jobs, 'community' : community}
	
	return render(request, 'classifieds/listings.html', context)



#THIS FUNCTION TAKES THE CATEGORY VARIABLE AND RENDERS ALL OF THOSE IN THE DATABSE ASSOCIATED WITH THAT CATEGORY	

def detail(request, types):
	latest_list = Classifieds.objects.filter(category = types).order_by('-pub_date')
	output = []

	for each_listing in latest_list:
		output.append(each_listing)
		


	context = {'output': output, 'types': types}
	return render(request, 'classifieds/detail.html', context)
"""
THE FOLLOWING IS CALLED WHEN A SPECIFIC CLASSIFIED IS CLICKED
IT SEARCHES THE DATABASE TO SEE IF IT EXISTS. IF SO, IT SEES IF ALL THE MODEL FIELDS HAVE BEEN FILLED
AND PASSES THOSE TO THE CONTEXT DICTIONARY WHICH WILL BE PASSED TO CLASSIFIEDS/SPECIFIC.HTML
"""
def specific(request, specific_id):
	object_database = Classifieds.objects.get(pk=specific_id)
	if object_database:
		spec_user = object_database.user.email
		spec_title = object_database.title
		spec_description = object_database.description
		context = {'spec_title': spec_title, 'spec_description': spec_description,
					 'spec_user': spec_user}
		if object_database.price:
			context['spec_price'] = object_database.price
		if object_database.photos:
			context['spec_photo'] = object_database.photos
		if object_database.photo2:
			context['spec_photo2'] = object_database.photo2
		if object_database.photo3:
			context['spec_photo3'] = object_database.photo3
		if object_database.photo4:
			context['spec_photo4'] = object_database.photo4
		return render(request, 'classifieds/specific.html', context)
		
	else:
		return HttpResponse("Sorry! The posting you are looking for does not exist.")

def post(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        pub_date = timezone.now()
        if form.is_valid():
        	data_dict = {'pub_date' : pub_date, 'title' : request.POST['title'], 
        	'category' : request.POST['category'], 'description' : request.POST['description'],
        	'user' : Users.objects.get(pk = request.session['id']), 
        	'school' : Schools.objects.get(pk=1)}

        	"""
        	BELOW CHECKS TO SEE IF THE FILES HAVE ACTUALLY BEEN UPLOADED...IF SO, IT ADDS THEM TO THE data_dict
        	FOR SOME REASON YOU HAVE TO USE REQUEST.FILES.GET('FILENAME', NONE) OR ELSE IT WON'T FIND THE KEY.
        	"""

        	if request.POST.get('price', None) != None:
        		price = request.POST.get('price', None)
        		if "$" not in price:
        			price = "$" + price

        		data_dict['price'] = price
        	if request.FILES.get('imagefile', None) != None:
        		data_dict['photos'] = request.FILES.get('imagefile', None)
        	if request.FILES.get('imagefile2', None) != None:
        		data_dict['photo2'] = request.FILES.get('imagefile2', None)
        	if request.FILES.get('imagefile3', None) != None:
        		data_dict['photo3'] = request.FILES.get('imagefile3', None)
        	if request.FILES.get('imagefile4', None) != None:
        		data_dict['photo4'] = request.FILES.get('imagefile4', None)

        	new_classified = Classifieds(**data_dict)
        	new_classified.save()
        	

        	return render(request, 'classifieds/success.html', {'new_classified': new_classified})
            
    else:
        form = DocumentForm() # A empty, unbound form




    # Render post page with the documents and the form
    return render_to_response(
        'classifieds/post.html',
        {'form': form, 'total_vars': total_vars},
        context_instance=RequestContext(request)
)

#HANDLES THE SEARCH FUNCTION.....GETS THE SEARCH DATA FROM LISTINGS.HTML
def search(request):

	if request.method == "POST":
		search_text = request.POST['search']
		if search_text:
			#ICONTAINS IS CASE INSENSITIVE 
			search_results = Classifieds.objects.filter(title__icontains = search_text)
		else:
			search_results = Classifieds.objects.filter(title__icontains = [])
	else: 
		search_results = []



	return render(request, 'classifieds/search_results.html', {'search_results': search_results})
