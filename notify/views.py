# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Notification, Schedule


def index(request):
    """ Notification app. home page. """
    all_notifications = Notification.objects.all()
    context = {'all_notifications': all_notifications,}
    return render(request, "notify/index.html", context)


def create(request):
    """ Notification creation page. """
    notify = Notification()
    notify.header = request.POST['header']
    notify.content = request.POST['content']
    notify.image_url = request.POST['image']
    notify.save()
    return HttpResponseRedirect("/notify/")
