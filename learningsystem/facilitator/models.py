from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Facilitator(models.Model):
	user = models.OneToOneField(User)

	middle_name = models.CharField(max_length=30, blank=True)
	nickname = models.CharField(max_length=30, blank=True)
	birthdate = models.DateField()
	contact_number = models.CharField(max_length=12, blank=True)

    #def __unicode__(self):
    #    return self.name