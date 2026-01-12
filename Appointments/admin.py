from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Appointment

# Register your models here.


@admin.register(Appointment)
class AppointmentsAdmin(admin.ModelAdmin):
    list_display = ("client", "dentists", "clinic", "appointment_time", "status")
    list_filter = ("status", "clinic")
    search_fields = ("client__user__username", "dentists__user__username", "comment")
