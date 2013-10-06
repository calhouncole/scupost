from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.views.generic.base import View
from schools.models import Schools
from django.shortcuts import render
from django.template import RequestContext, loader
from users.models import Users



#THIS CLASS TAKES THE USERS INPUT AND CHECKS TO SEE IF THE SCHOOL IS IN THE DATABSE

class Intro(View):
	


	def get(self, request):
	    return render(request, 'schools/intro.html')

#THE POST FUNCTION TAKES THE HTML OBJECTS SUBMITTED IN INTRO.HTML, CHECKS TO SEE IF USER IS IN DATABASE. IF SO, IT SETS THE SESSION
#ID AND REDIRECTS THE USER TO THE CLASSIFIEDS PAGE
# IF THE USER DOES NOT EXIST, IT ADDS THEM TO THE DATABASE AND THEN REDIRECTS TO THE CLASSIFIEDS PAGE

	def post(self, request):
		email = request.POST.get("email")
		password = request.POST.get("password")
		password2 = request.POST.get("password2")
		name = request.POST.get("name")
		count = email.find('@') 
		email = email[count+1 : ]
		user_database = Users.objects.filter(name = name).exists()
		if email == 'scu.edu':
			if password == password2:
				if user_database:
					user_database = Users.objects.get(name = name)
					request.session['id'] = user_database.id
					return HttpResponseRedirect('/classifieds')
				else:
					new_usr = Users(name = name, email = email, school = Schools.objects.get(pk=1))
					new_usr.save()
					request.session['id'] = new_usr.id
					return HttpResponseRedirect('/classifieds')

			else:
				return HttpResponse("Sorry, your passwords do not match")
		else:
			return HttpResponse("Sorry, that school is not in our database.")

			
		