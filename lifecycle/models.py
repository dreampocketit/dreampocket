from django.db import models

# Create your models here.
class LifeCycleCurve(models.Model):
	date = models.DateTimeField()
	number = models.IntegerField(default=0)
