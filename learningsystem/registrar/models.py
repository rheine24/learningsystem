from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Registrar(models.Model):
	user = models.OneToOneField(User)

	middle_name = models.CharField(max_length=30, blank=True)
	nickname = models.CharField(max_length=30, blank=True)
	birthdate = models.DateField()
	contact_number = models.CharField(max_length=12, blank=True)

	def __unicode__(self):
		return self.user.username

class LSInfo(models.Model):
	name = models.CharField(max_length=50)
	shortname = models.CharField(max_length=30)
	logo = models.ImageField(upload_to = "LSLogo")
	address = models.CharField(max_length=120)
	contact_number = models.CharField(max_length=12, blank=True)

	def __unicode__(self):
		return self.name
