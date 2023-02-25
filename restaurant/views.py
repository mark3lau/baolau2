from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.urls import reverse_lazy
from .models import Booking
from .forms import BookingForm, UpdateForm
from django.contrib import messages
from django.http import HttpResponseRedirect


class BookingList(generic.ListView):
    model = Booking
    queryset = Booking.objects.order_by('-booking_date')
    template_name = 'your_booking.html'
    paginate_by = 6
    

class HomePage(generic.ListView):
    template_name = 'index.html'
    queryset = Booking.objects.none()


class MakeBooking(CreateView):
    model = Booking
    form_class = BookingForm
    queryset = Booking.objects.order_by('-booking_date')
    template_name = 'make_booking.html'
    success_url = reverse_lazy('your_booking')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Your booking has been made successfully.')
        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request, 'There was an error processing your booking.')
        return response


class UpdateBooking(UpdateView):
    model = Booking
    fields = ('name', 'email', 'contact_number', 'number_of_people', 'booking_date', 'booking_time')
    template_name = 'update_booking.html'
    success_url = reverse_lazy('your_booking')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(name=self.request.user.username)

    def get_object(self, queryset=None):
        booking_id = self.kwargs['pk']
        return Booking.objects.get(pk=booking_id) 


class DeleteBooking(DeleteView):
    model = Booking
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('your_booking')

    def delete(self, request, *args, **kwargs):
        booking = self.get_object()
        messages.warning(request, f"Are you sure you want to delete the booking for {booking.name} on {booking.booking_date} at {booking.booking_time}?")
        return super().delete(request, *args, **kwargs)
