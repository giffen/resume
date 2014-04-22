from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect

from .models import Contact
from .forms import ContactForm

def home(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		
		if form.is_valid():
			# add to the database
			contact_us = form.save(commit=True)

			# send email to me
			subject = "Message from " + form.cleaned_data['full_name']
			from_email = form.cleaned_data['email']
			to_email = [settings.EMAIL_HOST_USER]
			message = form.cleaned_data['message']
			send_mail(subject, message, from_email, to_email, fail_silently=True)

			messages.success(request,"We will be in touch")

	return render_to_response("resume.html",locals(),context_instance=RequestContext(request))