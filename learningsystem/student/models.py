from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Student(models.Model):
	user = models.OneToOneField(User)

	middle_name = models.CharField(max_length=30, blank=True)
	nickname = models.CharField(max_length=30, blank=True)
	birthdate = models.DateField()
	contact_number = models.CharField(max_length=12, blank=True)
	photo = models.ImageField(upload_to = "PPicStd")

	def __unicode__(self):
		return self.user.username

class EnrolmentStatus(models.Model):
	student = models.ForeignKey('Student')
	event = models.ForeignKey('instructor.Event')
	status = models.BooleanField()

	def __unicode__(self):
		return self.student

class Attendance(models.Model):
	event = models.ForeignKey('instructor.Event')
	student = models.ForeignKey('Student')
	location = models.ForeignKey('facilitator.Location')
	date = models.DateField()
	time = models.TimeField()

	def __unicode__(self):
		return self.event + self.student

class RaiseHand(models.Model):	
	student = models.ForeignKey('Student')
	event = models.ForeignKey('instructor.Event')
	date = models.DateField()
	time = models.TimeField()

	def __unicode__(self):
		return self.event + self.student
	
