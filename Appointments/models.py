from django.db import models
from Dentists.models import Clinic
from Dentists.models import Dentists
from Client.models import Client

# Create your models here.


class Appointment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    dentists = models.ForeignKey(Dentists, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    appointment_time = models.TimeField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ("pending", "Pending"),
            ("confirmed", "Confirmed"),
            ("cancelled", "Cancelled"),
        ],
        default="pending",
    )
    comment = models.TextField()
