from django.db import models

class Appointment(models.Model):
    patient_name = models.CharField(max_length=100)
    appointment_date = models.DateTimeField()
    phone_number = models.CharField(max_length=15)
    is_confirmed = models.BooleanField(default=False)
    healthcare_provider = models.ForeignKey(
        'HealthcareProvider',  
        on_delete=models.CASCADE,
        default=1  
    )

    def __str__(self):
        return f'Appointment for {self.user} with {self.healthcare_provider} on {self.date_time}'


class HealthcareProvider(models.Model):  
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField()  
    
    def __str__(self):
         return self.name
    
