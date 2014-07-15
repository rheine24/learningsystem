from django.db import models

# Create your models here.

class Student(models.Model):
	student_number = models.IntegerField(unique=True)
	first_name = models.CharField(max_length=30)
	middle_name = models.CharField(max_length=30, blank=True)
	last_name = models.CharField(max_length=30)
	nickname = models.CharField(max_length=30, blank=True)
	birthdate = models.DateField()
	contact_number = models.CharField(max_length=12, blank=True)
	email_address = models.EmailField(max_length=75)
	password = models.CharField(max_length=20)
	#photo = models.ImageField()

    #def __unicode__(self):
    #    return self.name