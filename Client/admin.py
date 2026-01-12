from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Client, Order

# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("client", "dentists", "clinic", "appointment_time", "status")
    list_filter = ("status", "clinic")
    search_fields = ("client__user__username", "dentists__user__username")


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "visit", "age")
    list_filter = ("age",)
    search_fields = ("user__username", "name", "description")
