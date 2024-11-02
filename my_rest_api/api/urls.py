from django.urls import path
from .views import CarListCreateAPIView, CarDetailAPIView

urlpatterns = [
    path('cars/', CarListCreateAPIView.as_view(), name='car-list-create'),
    path('cars/<int:id>/', CarDetailAPIView.as_view(), name='car-detail'),
]