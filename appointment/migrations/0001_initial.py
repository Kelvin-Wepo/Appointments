# Generated by Django 4.2.4 on 2023-08-23 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=100)),
                ('appointment_date', models.DateTimeField()),
                ('phone_number', models.CharField(max_length=15)),
                ('is_confirmed', models.BooleanField(default=False)),
            ],
        ),
    ]
