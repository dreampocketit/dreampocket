from django.db import models

# Create your models here.
class RawData(models.Model):
	title = models.CharField(max_length=300, null=True)
	context = models.TextField()
	source = models.CharField(max_length=30)
	mainbody = models.BooleanField()
	date = models.DateTimeField()
	author = models.CharField(max_length=30)
	link = models.CharField(max_length=300)
