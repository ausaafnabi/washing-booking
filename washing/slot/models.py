from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Slot(models.Model):
    start= models.TimeField()
    end = models.TimeField()
    
class Machine(models.Model):
    macName = models.CharField(max_length=20,unique=True)
    slots = models.ManyToManyField(to=Slot)
    #address = models.CharField(max_length=80)
    roomNo = models.CharField(max_length=3)
    dormNo = models.CharField(max_length=2)
    comments = models.TextField()
    status = models.CharField(max_length=20)

class Booking(models.Model):
    Date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    machine_id = models.ForeignKey(Machine,on_delete=models.CASCADE)
    slot_id = models.ForeignKey(Slot, on_delete=models.CASCADE)
    comment = models.TextField()

class Booking(models.Model):
    Date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    machine_id = models.ForeignKey(Machine,on_delete=models.CASCADE)
    slot_id = models.ForeignKey(Slot, on_delete=models.CASCADE)
    comment = models.TextField()

class Status(models.Model):
    stat=models.CharField(max_length=20)

class perDy(models.Model):
    count = models.BooleanField(verbose_name="")

