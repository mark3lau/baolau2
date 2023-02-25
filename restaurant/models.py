from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True,)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    contact_number = models.CharField(max_length=20)
    number_of_people = models.IntegerField(default=1, validators=[MinValueValidator(1),MaxValueValidator(10)])
    booking_date = models.DateField()
    booking_time = models.TimeField()
    
    class Meta:
        ordering = ["-booking_date"]
    
