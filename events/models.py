# coding:utf8
from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=200)
    week = models.IntegerField()
    item = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name + ":" + self.item