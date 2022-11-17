from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from slot.models import Slot
# Create your views here.
@login_required()
def slot(request): 
    slot = Slot.objects.all()
    
    print(slot)
    context = {"slots": slot}
    if request.method == 'POST':
        pass
    else:
        pass
    return render(request,'app/slots.html',context=context)
