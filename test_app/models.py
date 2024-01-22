from django.db import models

class VehicleUser(models.Model):
    id = models.AutoField(primary_key=True)
    fName = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    status = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Address(models.Model):
    id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    pincode = models.CharField(max_length=10)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    long = models.DecimalField(max_digits=9, decimal_places=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(VehicleUser, on_delete=models.CASCADE)

class Vehicle(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    buy_date = models.DateField()
    color = models.CharField(max_length=255)
    last_service_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(VehicleUser, on_delete=models.CASCADE)

class Notification(models.Model):
    id = models.AutoField(primary_key=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class ServiceOrder(models.Model):
    id = models.AutoField(primary_key=True)
    booking_date = models.DateField()
    booking_time = models.TimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status_choices = [
        ('Pending', 'Pending'),
        ('In-Service', 'In-Service'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=20, choices=status_choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    user = models.ForeignKey(VehicleUser, on_delete=models.CASCADE)
    notification = models.OneToOneField(Notification, null=True, blank=True, on_delete=models.SET_NULL)

    def save(self, *args, **kwargs):
        # Check if the status has changed
        if self.pk:
            old_status = ServiceOrder.objects.get(pk=self.pk).status
            if old_status != self.status:
                # Create a notification when the status changes
                notification = Notification.objects.create(
                    message=f"Service order status changed to {self.status} for order ID {self.id}."
                )
                self.notification = notification
        super().save(*args, **kwargs)







 



 




