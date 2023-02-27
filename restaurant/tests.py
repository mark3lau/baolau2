from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from .models import Booking
from .forms import BookingForm

# Make Booking test case

class MakeBookingTest(TestCase):
    def setUp(self):
        # Create a user for testing purposes
        self.user = User.objects.create_user(
            username='testuser',
            password='password123'
        )

        # Set up valid booking data
        self.booking_data = {
            'name': 'Test User',
            'email': 'testuser@example.com',
            'contact_number': '1234567890',
            'number_of_people': 4,
            'booking_date': timezone.now().date() + timedelta(days=1),
            'booking_time': timezone.now().time(),
        }

        # Set up invalid booking data
        self.invalid_booking_data = {
            'name': '',
            'email': 'invalidemail',
            'contact_number': '12345',
            'number_of_people': -1,
            'booking_date': timezone.now().date(),
            'booking_time': timezone.now().time(),
        }

    def test_make_booking_view_with_valid_data(self):
        # Log in the user
        self.client.login(username='testuser', password='password123')

        # Make a booking with valid data
        response = self.client.post(reverse('make_booking'), data=self.booking_data)

        # Check that the booking was created
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Booking.objects.count(), 1)

    def test_make_booking_view_with_invalid_data(self):
        # Log in the user
        self.client.login(username='testuser', password='password123')

        # Make a booking with invalid data
        response = self.client.post(reverse('make_booking'), data=self.invalid_booking_data)

        # Check that the booking was not created and the form is invalid
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Booking.objects.count(), 0)
        self.assertFormError(response, 'form', 'name', 'This field is required.')
        self.assertFormError(response, 'form', 'email', 'Enter a valid email address.')
        self.assertFormError(response, 'form', 'contact_number', 'Ensure this value has at least 10 characters (it has 5).')
        self.assertFormError(response, 'form', 'number_of_people', 'Ensure this value is greater than or equal to 0.')
        self.assertFormError(response, 'form', 'booking_date', 'Select a valid choice. That choice is not one of the available choices.')


# Update booking test case

class UpdateBookingViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

        # Create a user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )

        # Create a booking for the user
        self.booking = Booking.objects.create(
            name='Test User',
            email='testuser@example.com',
            contact_number='1234567890',
            number_of_people=4,
            booking_date='2022-03-15',
            booking_time='12:00',
            user=self.user
        )

        self.url = reverse('update_booking', args=[self.booking.pk])

    def test_get_update_booking_form(self):
        # Login the user
        self.client.login(username='testuser', password='testpass')

        # Make a GET request to the update booking page
        response = self.client.get(self.url)

        # Check that the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Check that the form in the response context is an instance of UpdateForm
        self.assertIsInstance(response.context['form'], UpdateForm)

        # Check that the booking in the response context is the correct one
        self.assertEqual(response.context['booking'], self.booking)

        # Check that the response contains the expected text
        self.assertContains(response, 'Update booking')

    def test_update_booking(self):
        # Login the user
        self.client.login(username='testuser', password='testpass')

        # Make a POST request to update the booking
        data = {
            'name': 'Test User Updated',
            'email': 'testuser@example.com',
            'contact_number': '1234567890',
            'number_of_people': 6,
            'booking_date': '2022-03-15',
            'booking_time': '13:00',
        }
        response = self.client.post(self.url, data)

        # Check that the booking was updated in the database
        booking = Booking.objects.get(pk=self.booking.pk)
        self.assertEqual(booking.name, 'Test User Updated')
        self.assertEqual(booking.number_of_people, 6)
        self.assertEqual(booking.booking_time, '13:00')

        # Check that the response redirected to the user's booking page
        self.assertRedirects(response, reverse('your_booking'))

        # Check that the success message is displayed on the next page
        response = self.client.get(reverse('your_booking'))
        self.assertContains(response, 'Your booking has been updated successfully.')
