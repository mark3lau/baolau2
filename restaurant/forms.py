from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('name', 'email', 'contact_number', 'number_of_people', 'booking_date', 'booking_time')
        widgets = {
            'preferred_date': forms.DateInput(attrs={'type': 'date'}),
            'preferred_time': forms.TimeInput(attrs={'type': 'time'})
        }
        exclude = ['created_by_id']


