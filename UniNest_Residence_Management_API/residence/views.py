from rest_framework import generics, permissions, filters
from drf_yasg.utils import swagger_auto_schema
from django_filters.rest_framework import DjangoFilterBackend
from .models import Building, Room, Resident, MaintenanceRequest
from .serializers import BuildingSerializer, RoomSerializer, ResidentSerializer, MaintenanceRequestSerializer

# Building Views
class BuildingListCreateView(generics.ListCreateAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['name', 'address']
    ordering_fields = ['name', 'number_of_floors']

    @swagger_auto_schema(
        operation_description="List all buildings or create a new building.",
        responses={200: BuildingSerializer(many=True), 201: BuildingSerializer},
        request_body=BuildingSerializer
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=BuildingSerializer,
        responses={201: BuildingSerializer}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class BuildingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(
        operation_description="Retrieve, update or delete a building.",
        responses={200: BuildingSerializer, 204: None, 404: "Not Found"}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=BuildingSerializer,
        responses={200: BuildingSerializer, 404: "Not Found"}
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        responses={204: None, 404: "Not Found"}
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

# Similarly update Room and Resident views with Swagger documentation
# Room Views
class RoomListCreateView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['building', 'room_number']
    ordering_fields = ['room_number', 'floor']

    @swagger_auto_schema(
        operation_description="List all rooms or create a new room.",
        responses={200: RoomSerializer(many=True), 201: RoomSerializer},
        request_body=RoomSerializer
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=RoomSerializer,
        responses={201: RoomSerializer}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class RoomDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(
        operation_description="Retrieve, update or delete a room.",
        responses={200: RoomSerializer, 204: None, 404: "Not Found"}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=RoomSerializer,
        responses={200: RoomSerializer, 404: "Not Found"}
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        responses={204: None, 404: "Not Found"}
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

# Resident Views
class ResidentListCreateView(generics.ListCreateAPIView):
    queryset = Resident.objects.all()
    serializer_class = ResidentSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['room', 'name', 'email']
    ordering_fields = ['name']

    @swagger_auto_schema(
        operation_description="List all residents or create a new resident.",
        responses={200: ResidentSerializer(many=True), 201: ResidentSerializer},
        request_body=ResidentSerializer
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=ResidentSerializer,
        responses={201: ResidentSerializer}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class ResidentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resident.objects.all()
    serializer_class = ResidentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(
        operation_description="Retrieve, update or delete a resident.",
        responses={200: ResidentSerializer, 204: None, 404: "Not Found"}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=ResidentSerializer,
        responses={200: ResidentSerializer, 404: "Not Found"}
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        responses={204: None, 404: "Not Found"}
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

# Maintenance Request Views
class MaintenanceRequestListCreateView(generics.ListCreateAPIView):
    queryset = MaintenanceRequest.objects.all()
    serializer_class = MaintenanceRequestSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['resident', 'status']
    ordering_fields = ['created_at', 'status']

    @swagger_auto_schema(
        operation_description="List all maintenance requests or create a new request.",
        responses={200: MaintenanceRequestSerializer(many=True), 201: MaintenanceRequestSerializer},
        request_body=MaintenanceRequestSerializer
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=MaintenanceRequestSerializer,
        responses={201: MaintenanceRequestSerializer}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class MaintenanceRequestDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MaintenanceRequest.objects.all()
    serializer_class = MaintenanceRequestSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(
        operation_description="Retrieve, update or delete a maintenance request.",
        responses={200: MaintenanceRequestSerializer, 204: None, 404: "Not Found"}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=MaintenanceRequestSerializer,
        responses={200: MaintenanceRequestSerializer, 404: "Not Found"}
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        responses={204: None, 404: "Not Found"}
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)