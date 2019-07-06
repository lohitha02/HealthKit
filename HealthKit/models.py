from django.db import models
from django.core.files.storage import FileSystemStorage
from django.core.validators import MaxValueValidator

class Language(models.Model):
	name=models.CharField(max_length=20,verbose_name="Language Name", primary_key=True)
	def __str__(self):
		return self.name

class Doctor(models.Model):
	name=models.CharField(max_length=50, verbose_name="Name")
	age=models.IntegerField(validators=[MaxValueValidator(100)],verbose_name="Age")
	aadharNumber=models.IntegerField(validators=[MaxValueValidator(999999999999)],verbose_name="Aadhar Number")
	email=models.EmailField(blank=False, max_length=60, verbose_name="Email Address")
	specialization=models.CharField(max_length=50,verbose_name="Specialization")
	languages=models.ManyToManyField(Language)
	phoneNumber=models.IntegerField(validators=[MaxValueValidator(9999999999)],verbose_name="Phone Number")
	degree=models.TextField()
	class Meta:
		verbose_name="Doctor"
		verbose_name_plural="Doctor's"
	def __str__(self):
		return self.name
class Patient(models.Model):
	name=models.CharField(max_length=50, verbose_name="Name")
	age=models.IntegerField(validators=[MaxValueValidator(100)],verbose_name="Age")
	aadharNumber=models.IntegerField(validators=[MaxValueValidator(999999999999)],verbose_name="Aadhar Number")
	email=models.EmailField(blank=False, max_length=60, verbose_name="Email Address")
	languages=models.ManyToManyField(Language)
	phoneNumber=models.IntegerField(validators=[MaxValueValidator(9999999999)],verbose_name="Phone Number")
	previousDoctors=models.ManyToManyField(Doctor)
	class Meta:
		verbose_name="Patient"
		verbose_name_plural="Patient's"
	def __str__(self):
		return self.name
