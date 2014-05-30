from django.db import models

# Create your models here.
class Device(models.Model):
	Number	=	models.CharField(max_length=10)
	Name    =   models.CharField(max_length=50)
	Amount	=	models.CharField(max_length=10)
	Price   =   models.CharField(max_length=20)
	Donater	=	models.CharField(max_length=50)
	Avaliable =	models.BooleanField()
	LastCheckTime = models.DateField(blank=True,null=True)
	Remark	=	models.TextField(blank=True)

	def __unicode__(self):
		return self.Name

