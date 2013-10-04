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

	def post(self, request):
		answer = request.POST.get("email")
		password = request.POST.get("password")
		password2 = request.POST.get("password2")
		name = request.POST.get("name")
		count = answer.find('@') 
		answer = answer[count+1 : ]
		user_database = Users.objects.filter(name = name).exists()
		if answer == 'scu.edu':
			if password == password2:
				if user_database:
					user_database = Users.objects.get(name = name)
					request.session['id'] = user_database.id
					return HttpResponseRedirect('/classifieds')
				else:
					return HttpResponse("hello")
			else:
				return HttpResponse("Sorry, your passwords do not match")
		else:
			return HttpResponse("Sorry, that school is not in our database.")
			#return HttpResponseRedirect('/classifieds', context)
		
			#new_usr = Users(name = name, email = answer, school = Schools.objects.get( pk = 1))
			#new_usr.save()
			#return HttpResponse(new_usr.name)
			
		