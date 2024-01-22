from django.shortcuts import render

from rest_framework import viewsets
from .models import VehicleUser, Address, Vehicle, ServiceOrder, Notification
from .serializers import VehicleUserSerializer, AddressSerializer, VehicleSerializer, ServiceOrderSerializer, NotificationSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import status

class SignupAPIView(APIView):
    def post(self, request):
 
        # Create a login user for internal use
        try:
            user = User.objects.create_superuser(
                username=request.data['username'],
                email=request.data['email'],
                password=request.data['password']
            )
            return Response({'detail': 'Admin user created successfully.'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class VehicleUserViewSet(viewsets.ModelViewSet):
    queryset = VehicleUser.objects.all()
    serializer_class = VehicleUserSerializer
    permission_classes = [IsAuthenticated]

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated]

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [IsAuthenticated]

class ServiceOrderViewSet(viewsets.ModelViewSet):
    queryset = ServiceOrder.objects.all()
    serializer_class = ServiceOrderSerializer
    permission_classes = [IsAuthenticated]

class NotificationAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notifications = Notification.objects.all()
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
