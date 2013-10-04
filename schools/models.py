from django.db import models



class Schools(models.Model):
	name = models.CharField(max_length=200)
	email = models.CharField(max_length = 200)
	location = models.CharField(max_length=200)
	enrollment = models.BigIntegerField()
	def __unicode__(self):
		return self.name
