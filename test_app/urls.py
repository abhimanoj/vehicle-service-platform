from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from .views import VehicleUserViewSet, AddressViewSet, VehicleViewSet, ServiceOrderViewSet, SignupAPIView, NotificationAPIView

router = DefaultRouter()
router.register(r'vehicle-users', VehicleUserViewSet)
router.register(r'addresses', AddressViewSet)
router.register(r'vehicles', VehicleViewSet)
router.register(r'service-orders', ServiceOrderViewSet)

urlpatterns = [
    path('signup/', SignupAPIView.as_view(), name='signup'),
    path('login/', obtain_auth_token, name='api_token_auth'),
    path('', include(router.urls)),
    path('notifications/', NotificationAPIView.as_view(), name='notification-list'),

]
