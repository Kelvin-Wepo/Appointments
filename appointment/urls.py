from django.urls import path
from . import views

app_name = 'appointments'

urlpatterns = [
    path('', views.list_available_appointments, name='list'),
    path('', views.book_appointment, name='book'),
    path('confirm/<int:appointment_id>/', views.confirm_appointment, name='confirm'),
]
