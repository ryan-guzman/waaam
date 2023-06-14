from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist


class ActivityChoice(models.Model):
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.description


class VolunteerRecord(models.Model):
    activity = models.ForeignKey(ActivityChoice, blank=False, on_delete=models.CASCADE)
    hours = models.FloatField(blank=False)
    date = models.DateField(auto_now=False, auto_now_add=False, blank=False)
    # supervisor = models.CharField(max_length=256, blank=False)
    description = models.CharField(max_length=1000, blank=True, default='')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "Owner: {}, Date: {}, Activity: {}".format(self.owner, self.date, self.activity)