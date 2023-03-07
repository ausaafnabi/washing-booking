from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
class Slot(models.Model):
    start = models.TimeField(datetime.now())
    end = models.TimeField(datetime.now())


class Machine(models.Model):
    macName = models.CharField(default='', max_length=20,unique=True)
    slots = models.ManyToManyField(default=1, to=Slot)
    #address = models.CharField(max_length=80)
    roomNo = models.CharField(default='', max_length=3)
    dormNo = models.CharField(default='', max_length=2)
    comments = models.TextField(default='')
    status = models.CharField(default='', max_length=20)


class Booking(models.Model):
    Date = models.DateField(datetime.now())
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    machine_id = models.ForeignKey(Machine, on_delete=models.CASCADE)
    slot_id = models.ForeignKey(Slot, on_delete=models.CASCADE)
    comment = models.TextField(default='')


class Booking(models.Model):
    Date = models.DateField(datetime.now())
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    machine_id = models.ForeignKey(Machine, on_delete=models.CASCADE)
    slot_id = models.ForeignKey(Slot, on_delete=models.CASCADE)
    comment = models.TextField(default='')


class Status(models.Model):
    stat = models.CharField(default='', max_length=20)


class perDy(models.Model):
    count = models.BooleanField(default=True, verbose_name="")

