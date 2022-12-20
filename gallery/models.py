from django.db import models

# Create your models here.
class Collection(models.Model):
	name = models.CharField(max_length=150)
	description = models.CharField(max_length = 150)
	image = models.ImageField(upload_to='images/')
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name
		
	
class Item(models.Model):
	collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='items' )
	image = models.ImageField(upload_to='images/')
	created_at = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.collection.name+' '+str(self.id)
	
