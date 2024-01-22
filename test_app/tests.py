from django.test import TestCase

from django.contrib.auth.models import User
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from .models import VehicleUser, Address, Vehicle, ServiceOrder

class APITests(APITestCase):
    def setUp(self):
        # Create a user for authentication
        self.admin_user = User.objects.create_superuser(
            username='admin',
            password='adminpassword',
            email='admin@example.com'
        )

        # Authenticate the client
        self.client = APIClient()
        self.client.force_authenticate(user=self.admin_user)

        # Create some initial data for testing
        self.vehicle_user = VehicleUser.objects.create(
            fName='Test',
            lname='Lname',
            email='test@gmail.com',
            phone='1234567890',
            status='Active',
            is_active=True
        )

        self.address = Address.objects.create(
            address='123 Loc St',
            state='MP',
            city='Bhopal',
            pincode='462042',
            lat='11.1234',
            long='22.1234',
            user=self.vehicle_user
        )

        self.vehicle = Vehicle.objects.create(
            type='Car',
            model='Sedan',
            buy_date='2022-01-01',
            color='Blue',
            last_service_date='2022-02-01',
            user=self.vehicle_user
        )

        self.service_order = ServiceOrder.objects.create(
            booking_date='2022-03-01',
            booking_time='12:00:00',
            amount='100.00',
            status='Pending',
            vehicle=self.vehicle,
            user=self.vehicle_user
        )

    def test_signup_admin(self):
        url = '/api/signup/'
        data = {
            'username': 'admin_test',
            'email': 'admin_test@gmail.com',
            'password': 'admin@123'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verify the user was created
        new_admin = User.objects.get(username='admin_test')
        self.assertEqual(new_admin.email, 'admin_test@gmail.com')