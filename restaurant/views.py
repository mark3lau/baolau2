from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Booking

class BookingList(generic.ListView):
    model = Booking
    queryset = Booking.objects.order_by('-booking_date')
    template_name = 'booking.html'
    paginate_by = 6
    

class HomePage(generic.ListView):
    template_name = 'index.html'