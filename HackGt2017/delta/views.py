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
	p = Profile(talk = request.POST['talk'], sleep = request.POST['sleep'],
		drink = request.POST['drink'], child = request.POST['child'],
		username = request.POST['name'])
	p.save()

	seat_list = Seat.objects.order_by('number')
	comp = {}
	for x in range(len(seat_list)):
		if seat_list[x].profile:
			comp[seat_list[x]] = []
			if x-1 >= 0 and not seat_list[x-1].profile:
				comp[seat_list[x]].append(seat_list[x-1])
			if x+1 < len(seat_list) and not seat_list[x+1].profile:
				comp[seat_list[x]].append(seat_list[x+1])

	rec_list = recSelect(comp, seat_list, p)
		 
	context = {"seat_list" : seat_list, "rec_list": rec_list, "profile": p}
	return render(request, 'seats.html', context)

def recSelect(dict, seat_list, profile):
	rec_list = {}
	for y in dict.keys():
		taken = y.profile
		percent_match = ((1 if (taken.talk == (profile.talk == "True")) else 0) + (1 if (taken.sleep == (profile.sleep == "True")) else 0) + 
						(1 if (taken.drink == (profile.drink == "True")) else 0) + (1 if (taken.child == (profile.child == "True")) else 0)) / 4.0
		for open_seat in dict[y]:
			if open_seat in rec_list:
				rec_list[open_seat] = (rec_list[open_seat] + percent_match) / 2.0
			else:
				rec_list[open_seat] = percent_match
	for x in seat_list:
		if not x in rec_list:
			rec_list[x] = 1.0
	return rec_list 

def seatFinish(request):
	# s = Seat(number=request.POST["number"], profile=request.POST["profile"])
	# s.save()
	print("profile", request.POST["profile"], "seat", request.POST["seat"])
	p = Profile.objects.get(id=request.POST["profile"])
	s = Seat.objects.get(number=request.POST["seat"])
	s.profile = p
	s.save()

	return HttpResponseRedirect('/')
