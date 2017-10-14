# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Profile(models.Model):
	username = models.CharField(max_length=200, default="username")
	talk = models.NullBooleanField()
	sleep = models.NullBooleanField()
	drink = models.NullBooleanField()
	child = models.NullBooleanField()

class Seat(models.Model):
	number = models.IntegerField(default=0)
	profile = models.ForeignKey(
			'Profile',
			on_delete=models.SET_NULL,
			null=True,
			blank=True
		)

