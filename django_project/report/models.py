from django.db import models

# Create your models here.

class Report(models.Model):
	name=models.CharField(max_length=100)
	aemail=models.EmailField()
	category=models.CharField(max_length=25)
