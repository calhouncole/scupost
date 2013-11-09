from django.db import models

from users.models import Users
from schools.models import Schools


class Classifieds(models.Model):
	category = models.CharField(max_length = 200)
	user = models.ForeignKey(Users)
	school = models.ForeignKey(Schools)
	title = models.CharField(max_length = 200)
	pub_date = models.DateTimeField('date published')
	photos = models.ImageField(upload_to = 'documents/%Y/%m/%d', null = True, blank = True)
	photo2 = models.ImageField(upload_to = 'documents/%Y/%m/%d', null = True, blank = True)
	photo3 = models.ImageField(upload_to = 'documents/%Y/%m/%d', null = True, blank = True)
	photo4 = models.ImageField(upload_to = 'documents/%Y/%m/%d', null = True, blank = True)
	description = models.TextField()
	def __unicode__(self):
		return self.title
