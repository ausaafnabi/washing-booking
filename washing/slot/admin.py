from django.contrib import admin
from slot.models import Slot,Booking,Machine

class SlotAdmin(admin.ModelAdmin):
    pass
class BookingAdmin(admin.ModelAdmin):
    pass
class MachineAdmin(admin.ModelAdmin):
    pass

admin.site.register(Slot, SlotAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Machine, MachineAdmin)