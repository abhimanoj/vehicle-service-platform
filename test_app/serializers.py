from rest_framework import serializers
from .models import VehicleUser, Address, Vehicle, ServiceOrder, Notification

class VehicleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleUser
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class ServiceOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceOrder
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'