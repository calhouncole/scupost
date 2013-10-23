from django.db import models

from users.models import Users
from schools.models import Schools


class Classifieds(models.Model):
	category = models.CharField(max_length = 200)
	user = models.ForeignKey(Users)
	school = models.ForeignKey(Schools)
	title = models.CharField(max_length = 200)
	photos = models.ImageField(upload_to = 'documents/%Y/%m/%d')
	description = models.TextField()
	def __unicode__(self):
		return self.title


class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
