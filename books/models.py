from django.db import models

# Create your models here.
class Publisher(models.Model):
	Name	= 	models.CharField(max_length=30)
	def __unicode__(self):
		return self.Name

class Book(models.Model):
	Number	=	models.CharField(max_length=50)
	Types	=	models.CharField(max_length=100)
	Title	=	models.CharField(max_length=100)
#	Bookhash=	models.CharField(max_length=100)
	Isbn	=	models.CharField(max_length=100)
	Price	=	models.CharField(max_length=50)
	Publish	=	models.ForeignKey(Publisher)	
	Owner	=	models.CharField(max_length=50)
	Ordered	=	models.BooleanField(default=False)
	Keeper	=	models.TextField(blank=True)
	Keepertel = models.CharField(max_length=50,blank=True,null=True)
	Endtime	= 	models.DateField(blank=True,null=True)
	def __unicode__(self):
		return self.Title
