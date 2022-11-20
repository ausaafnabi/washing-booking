from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from slot.models import Slot,Machine
# Create your views here.
@login_required()
def slot(request): 
    slot = Slot.objects.all()
    context = {"slots": slot}
    if request.method == 'POST':
        pass
    else:
        pass
    return render(request,'app/slots.html',context=context)

@login_required()
def machines(request):
    machine = Machine.objects.all()
    context = {"machines":machine}
    
    return render(request,"app/machines.html",context=context)