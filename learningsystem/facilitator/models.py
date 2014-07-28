from django.contrib.auth.models import User
from django.db import models
from instructor.models import *

# Create your models here.

class Facilitator(models.Model):
	user = models.OneToOneField(User)

	middle_name = models.CharField(max_length=30, blank=True)
	nickname = models.CharField(max_length=30, blank=True)
	birthdate = models.DateField()
	contact_number = models.CharField(max_length=12)

	def __unicode__(self):
		return self.user.username + " " + self.user.last_name

class Location(models.Model):
	room = models.CharField(max_length=30)
	floor = models.CharField(max_length=3)
	bldg = models.CharField(max_length=50)
	street_address = models.CharField(max_length=75)
	town_or_city = models.CharField(max_length=50)
	province = models.CharField(max_length=50)
	country = models.CharField(max_length=30)

	def __unicode__(self):
		return self.bldg

class FaciLocEvent(models.Model):
	facilitator = models.ForeignKey('Facilitator')
	location = models.ForeignKey('Location')
	event = models.ForeignKey('instructor.Event')
	date = models.DateField()
	time = models.TimeField()

	def __unicode__(self):
		return self.facilitator.user.username + " | " + self.location.bldg + " | " + self.event.event_code