from django.db import models

# Create your models here.
class Publisher(models.Model):
	Name	= 	models.CharField(max_length=30)
	
	def __unicode__(self):
		return self.Name

class Book(models.Model):
	Types	=	models.CharField(max_length=100)
	Title	=	models.CharField(max_length=100)
	Price	=	models.CharField(max_length=50)
	Publish	=	models.ForeignKey(Publisher)	
	Source	=	models.CharField(max_length=50)
	Keeper	=	models.TextField(blank=True)
	Endtime	= 	models.DateField(blank=True,null=True)

	def __unicode__(self):
		return self.Title

