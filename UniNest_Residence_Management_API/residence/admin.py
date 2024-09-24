# residence/admin.py

from django.contrib import admin
from .models import Building, Room, Resident, MaintenanceRequest

@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('building', 'number', 'room_type', 'is_occupied')

@admin.register(Resident)
class ResidentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'room')

@admin.register(MaintenanceRequest)
class MaintenanceRequestAdmin(admin.ModelAdmin):
    list_display = ('resident', 'description', 'priority', 'status', 'date_requested', 'is_completed')
