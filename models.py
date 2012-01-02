from django.db import models

class Image(models.Model):
	text = models.CharField(max_length=50, blank = True, null = True)
	image = models.ImageField(upload_to = 'Images')
	def __unicode__(self):
		if self.text:
			return self.text
		else:
			return self.image.path
	
class Gallery(models.Model):
	title = models.CharField(max_length = 50)
	images = models.ManyToManyField(Image)
	def __unicode__(self):
		return self.title
		
	def get_first(self):
		return self.images.all()[0].image
		
	def get_first_caption(self):	
		return self.images.all()[0].text
		
	def get_all(self):
		return self.images.all()