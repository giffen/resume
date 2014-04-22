from django.db import models
from django.utils.encoding import smart_unicode

class Contact(models.Model):
	full_name = models.CharField(max_length=200, null=True, blank=False)
	email = models.EmailField(null=False, blank=False)
	message = models.CharField(max_length=600, null=True, blank=False)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	update = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return smart_unicode(self.email)

