from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator, MaxValueValidator


class Booking(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    number_of_people = models.IntegerField(default=1, validators=[MinValueValidator(1),MaxValueValidator(10)])
    booking_date = models.DateField()
    booking_time = models.TimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ["-booking_date"]
