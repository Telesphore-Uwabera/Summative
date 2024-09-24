from django.urls import path
from .views import (
    BuildingListCreateView, 
    BuildingDetailView, 
    RoomListCreateView, 
    RoomDetailView, 
    ResidentListCreateView, 
    ResidentDetailView, 
    MaintenanceRequestListCreateView, 
    MaintenanceRequestDetailView
)

urlpatterns = [
    # Endpoint to list all buildings and create a new building
    path('buildings/', BuildingListCreateView.as_view(), name='building-list-create'),
    
    # Endpoint to retrieve, update, or delete a specific building by its ID (pk)
    path('buildings/<int:pk>/', BuildingDetailView.as_view(), name='building-detail'),
    
    # Endpoint to list all rooms and create a new room
    path('rooms/', RoomListCreateView.as_view(), name='room-list-create'),
    
    # Endpoint to retrieve, update, or delete a specific room by its ID (pk)
    path('rooms/<int:pk>/', RoomDetailView.as_view(), name='room-detail'),
    
    # Endpoint to list all residents and create a new resident
    path('residents/', ResidentListCreateView.as_view(), name='resident-list-create'),
    
    # Endpoint to retrieve, update, or delete a specific resident by their ID (pk)
    path('residents/<int:pk>/', ResidentDetailView.as_view(), name='resident-detail'),
    
    # Endpoint to list all maintenance requests and create a new request
    path('maintenancerequests/', MaintenanceRequestListCreateView.as_view(), name='maintenance-list-create'),
    
    # Endpoint to retrieve, update, or delete a specific maintenance request by its ID (pk)
    path('maintenancerequests/<int:pk>/', MaintenanceRequestDetailView.as_view(), name='maintenance-detail'),
]
