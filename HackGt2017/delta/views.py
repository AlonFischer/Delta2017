# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect, HttpResponse

from django.shortcuts import render
from delta.models import Profile, Seat

# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class AboutPageView(TemplateView):
	template_name = "about.html"

def surveyProcess(request):
	Profile(talk = request.POST['talk'], sleep = request.POST['sleep'],
		drink = request.POST['drink'], child = request.POST['child'],
		username = request.POST['name']).save()
	return HttpResponseRedirect("about")