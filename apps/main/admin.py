from django.contrib import admin
from .models import Reservation

class ReservAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', ]


admin.site.register(Reservation, ReservAdmin)

# Register your models here.
