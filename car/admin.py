from django.contrib import admin
from  car.models import Registration, Booking,Form
# Register your models here.

admin.site.register(Registration)
admin.site.register(Booking)    
admin.site.register(Form) 
