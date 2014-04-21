from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect

def home(request):

	return render_to_response("resume.html",locals(),context_instance=RequestContext(request))