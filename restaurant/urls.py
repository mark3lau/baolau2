from . import views
from django.urls import path
from .views import MakeBooking, UpdateBooking, DeleteBooking


urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('your_booking', views.BookingList.as_view(), name='your_booking'),
    path('make_booking', views.MakeBooking.as_view(), name='make_booking'),
    path('update_booking/<int:pk>', views.UpdateBooking.as_view(), name='update_booking'),
    path('delete_booking/<int:pk>', views.DeleteBooking.as_view(), name='delete_booking'),
    path('menu', views.Menu.as_view(), name='menu'),
]