from django.db import models

# Create your models here.
class Metadata(models.Model):

	SKU	= models.IntegerField(blank=False, null=True)
	NAME = models.CharField(max_length=40,default='')
	LOCATION = models.CharField(max_length=40,default='')
	DEPARTMENT = models.CharField(max_length=45)
	CATEGORY = models.CharField(max_length=40,default='')
	SUBCATEGORY = models.CharField(max_length=40,default='')
	class Meta:
		managed = True
