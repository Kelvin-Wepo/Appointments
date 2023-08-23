# appointments/views.py

from django.shortcuts import render, redirect
from .models import Appointment
from .forms import AppointmentForm
import africastalking
from django.conf import settings

def list_available_appointments(request):
    available_appointments = Appointment.objects.filter(is_confirmed=False)
    return render(request, 'appointments/available_appointments.html', {'appointments': available_appointments})

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()

            # Send SMS confirmation using Africa's Talking API
            africastalking.initialize(username=settings.AFRICAS_TALKING_USERNAME, api_key=settings.AFRICAS_TALKING_API_KEY)
            sms = africastalking.SMS
            message = f"Your appointment on {appointment.appointment_date} has been confirmed."
            phone_number = appointment.phone_number
            response = sms.send(message, [phone_number])

            return redirect('appointments:confirm', appointment_id=appointment.id)
    else:
        form = AppointmentForm()

    return render(request, 'appointments/book_appointment.html', {'form': form})

def confirm_appointment(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    return render(request, 'appointments/confirm_appointment.html', {'appointment': appointment})
