import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'washing.settings')

import django
django.setup()

from login import *
from slot.models import Machine, Slot 
import datetime
def Population():
    machine={}
    d = []
    for i in range (0,23):
        d.append(datetime.time(i, 0, 0))
    d.append(datetime.time(0,0,0))
    sl = {}
    print("Adding Slots of 1 Hour....")
    for i in range(0,23):
        addSlot(d[i],d[i+1])
    slot = Slot.objects.all()
    print(slot)
    print("Adding Test Machine....")
    addMachine(name="Machine No.1",address="Room No. X",comment="Test",status="available",slots=slot)

def addMachine(name,address,comment,status,slots):
    mac = Machine.objects.get_or_create(macName=name)[0]
    mac.address = address
    mac.comments = comment
    mac.status = status
    for s in slots:
        mac.slots.add(s)
    mac.save()
    return mac

def addSlot(st,en):
    slot = Slot.objects.get_or_create(start=st,end=en)[0]
    slot.save()
    return slot

if __name__=="__main__":
    print("Initializing the Population Script...")
    Population()