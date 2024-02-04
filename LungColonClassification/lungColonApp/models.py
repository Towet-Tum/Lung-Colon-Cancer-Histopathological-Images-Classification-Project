from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class PatientRecords(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="Patient")
    pred_class = models.CharField(max_length=100)
    score = models.FloatField()
    desc = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.patient.username


class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    appointment_date = models.DateField()
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return self.email


class Conctact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    tel = models.CharField(max_length=13)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.full_name
