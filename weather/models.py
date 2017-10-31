from django.db import models

# Create your models here.
class Weather(models.Model):
	loc1=models.CharField(max_length=50,blank=False)
	loc2=models.CharField(max_length=50,blank=False)

