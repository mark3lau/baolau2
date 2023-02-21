from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('your_booking', views.BookingList.as_view(), name='your_booking'),
    path('make_booking', views.MakeBooking.as_view(), name='make_booking'),
]