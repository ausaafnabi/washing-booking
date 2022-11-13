from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Slot(models.Model):
    machineTime = models.TimeField()

class Booking(models.Model):
    Date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slot_id = models.ForeignKey(Slot, on_delete=models.CASCADE)

