from django.db import models

# Create your models here.
class RawData(models.Model):
	title = models.CharField(max_length=3000)
	source = models.CharField(max_length=3000)
	context = models.CharField(max_length=3000)
	date = models.DateTimeField()
	author = models.CharField(max_length=3000)
	link = models.CharField(max_length=3000)
