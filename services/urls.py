from django.urls import path
from . import views

urlpatterns = [
    path('', views.services, name='services'),
    path('service_list/', views.service_list, name='service_list'),    
    path('provider/<int:provider_id>/', views.service_provider, name='service_provider'),
]