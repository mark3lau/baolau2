from django.shortcuts import render, redirect
from django.views import generic, View
from .models import Booking
from .forms import BookingForm


class BookingList(generic.ListView):
    model = Booking
    queryset = Booking.objects.order_by('-booking_date')
    template_name = 'your_booking.html'
    paginate_by = 6
    

class HomePage(generic.ListView):
    template_name = 'index.html'
    queryset = Booking.objects.none()


class MakeBooking(generic.ListView):
    model = Booking
    queryset = Booking.objects.order_by('-booking_date')
    template_name = 'make_booking.html'
    paginate_by = 6


def booking_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'templates/your_booking.html')
    else:
        form = BookingForm()
    return render(request, 'templates/make_booking.html', {'form': form})
