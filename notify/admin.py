# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Notification, Schedule
# Register your models here.
admin.site.register(Notification)
admin.site.register(Schedule)