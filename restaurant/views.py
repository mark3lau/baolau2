from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.urls import reverse_lazy
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


class MakeBooking(CreateView):
    model = Booking
    form_class = BookingForm
    queryset = Booking.objects.order_by('-booking_date')
    template_name = 'make_booking.html'
    paginate_by = 6
    
    form = BookingForm()

    def booking_view(request):
        if request.method == 'POST':
            form = BookingForm(request.POST)
            context = {
                'form': form
            }
            if form.is_valid():
                form.save()
            return render(request, 'your_booking.html', context)
        else:
            return render (request, 'make_booking.html')


class UpdateBooking(UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = 'your_booking.html'
    success_url = reverse_lazy('your_booking')


class DeleteBooking(DeleteView):
    model = Booking
    template_name = 'your_booking.html'
    success_url = reverse_lazy('your_booking')


    
 


# {'form':form}