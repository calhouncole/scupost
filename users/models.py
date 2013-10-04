from django.db import models
from schools.models import Schools

class Users(models.Model):
	name = models.CharField(max_length=200)
	email = models.CharField(max_length = 200)
	school = models.ForeignKey(Schools)
	def __unicode__(self):
		return self.name
	