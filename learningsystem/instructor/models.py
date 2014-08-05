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
		
	def getName(self):
		return self.user.first_name + " " + self.middle_name + " " + self.user.last_name

class Event(models.Model):
	name = models.CharField(max_length = 50)
	event_code = models.CharField(max_length = 15, blank=True) #From Admin must be required
	description = models.CharField(max_length = 160, blank=True)
	instructor = models.ForeignKey('Instructor') #Get from User
	start_date = models.DateField()
	end_date = models.DateField() #akaRepeatUntil
	start_time = models.TimeField()
	end_time = models.TimeField()
	frequency = models.ForeignKey('Frequency')  #Monthly/weekly #Default = 0
	#rate_questions = models.ForeignKey('') #blank = True #Edit mode
	lecture = models.FileField(upload_to = "Lecture/%Y/%m", blank=True) #Edit Mode
	enlistment_type = models.BooleanField(default=True) #default = free for all (True)
	approval_status = models.BooleanField(default=False) #default = not yet approved (False)

	def __unicode__(self):
		return self.name

class Frequency(models.Model):
	description = models.CharField(max_length = 15)

	def __unicode__(self):
		return self.description