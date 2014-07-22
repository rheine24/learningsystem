from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Instructor(models.Model):
	user = models.OneToOneField(User)

	middle_name = models.CharField(max_length=30, blank=True)
	nickname = models.CharField(max_length=30, blank=True)
	birthdate = models.DateField()
	contact_number = models.CharField(max_length=12, blank=True)
	photo = models.ImageField(upload_to = "PPicInst")

	def __unicode__(self):
		return self.user.username

class Event(models.Model):
	name = models.CharField(max_length = 50)
	event_code = models.CharField(max_length = 15)
	description = models.CharField(max_length = 160)
	instructor = models.ForeignKey('Instructor')
	start_date = models.DateField()
	end_date = models.DateField()
	start_time = models.TimeField()
	end_time = models.TimeField()
	#rate_questions = models.ForeignKey('')
	#frequency = models.ForeignKey('')
	lecture = models.FileField(upload_to = "Lecture/%Y/%m")
	enlistment_type = models.BooleanField()
	approval_status = models.BooleanField()

	#def __unicode__(self):
	#	return self.user.event_code
		