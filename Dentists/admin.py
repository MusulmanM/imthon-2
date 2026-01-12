from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Clinic, Dentists, WorkingHours


# Register your models here.
@admin.register(Clinic)
class ClinicAdmin(admin.ModelAdmin):
    list_display = ("name", "location")
    list_filter = ("name", "location")
    search_fields = ("name", "location")


@admin.register(Dentists)
class DentistsAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "age")
    list_filter = ("age",)
    search_fields = ("user__username", "name")


@admin.register(WorkingHours)
class WorkingHoursAdmin(admin.ModelAdmin):
    list_display = ("dentists", "day", "start_date", "end_date")
    list_filter = ("day",)
    search_fields = ("dentists__user__username",)
