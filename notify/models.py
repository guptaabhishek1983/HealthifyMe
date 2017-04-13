# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import URLValidator, MaxLengthValidator, MinLengthValidator

notification_status = [(-1, 'DELIVERY FAILED'), (0, 'NOT DELIVERED'), (1, 'IN PROGRESS'), (2, 'DELIVERED')]
notification_status_dict = dict((v, k) for k, v in notification_status)


class Notification(models.Model):
    """ Notification model """
    header = models.CharField(max_length=150,
                              validators=[MinLengthValidator(20, "Header cannot be less then 20 characters."),
                                          MaxLengthValidator(150, "Header cannot be more than 150 characters.")])
    content = models.CharField(max_length=300,
                               validators=[MinLengthValidator(20, "Content cannot be less then 20 characters."),
                                           MaxLengthValidator(300, "Content cannot be more than 300 characters.")])
    image_url = models.TextField(validators=[URLValidator()])

    def __str__(self):
        return "#" + str(self.id) + "-" + self.header


class Schedule(models.Model):
    """ schedule model """
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE)
    time = models.DateTimeField()
    status = models.PositiveSmallIntegerField(choices=notification_status,
                                              default=notification_status_dict['NOT DELIVERED'])

    def __str__(self):
        if self.status == notification_status_dict['NOT DELIVERED']:
            return "'" + self.notification.header + "' is scheduled for:" + self.time.strftime("%d-%m-%Y %H:%M")
