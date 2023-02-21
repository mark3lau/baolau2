from django.contrib import admin
from .models import Booking
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):

    list_filter = ('booking_date', 'booking_time')
    list_display = ('booking_date', 'booking_time')
    search_fields = ['booking_date', 'booking_time']
    # summernote_fields = ('content')

