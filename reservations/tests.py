from django.test import TestCase
from django.core import exceptions
from datetime import datetime

from .models import Reservation
from cars.models import Car

class ReservationTestCase(TestCase):
    def setUp(self):
        self.car = Car.objects.create(
            uid="C111",
            make="FirstMake",
            model="FirstModel",
        )
        self.first_reservation = Reservation.objects.create(
            car=self.car,
            starts_at=datetime.fromisoformat("2023-09-18 10:22:33+00"),
            duration=38,
        )
        self.second_reservation = Reservation.objects.create(
            car=self.car,
            starts_at=datetime.fromisoformat("2023-09-18 11:20:00+00"),
            duration=30,
        )

    def test_start_to_end_datetimes(self):
        expected_starts_at = datetime.fromisoformat("2023-09-18 10:22:00+00")
        expected_ends_at = datetime.fromisoformat("2023-09-18 10:59:59+00")
        self.assertEqual(self.first_reservation.starts_at, expected_starts_at)
        self.assertEqual(self.first_reservation.ends_at, expected_ends_at)

    def test_reservation_created_when_available_before(self):
        reservation = Reservation.objects.create(
            car=self.car,
            starts_at=datetime.fromisoformat("2023-09-18 10:01:00+00"),
            duration=21,
        )
        expected_ends_at = datetime.fromisoformat("2023-09-18 10:21:59+00")
        self.assertEqual(reservation.ends_at, expected_ends_at)

    def test_reservation_created_when_available_between(self):
        reservation = Reservation.objects.create(
            car=self.car,
            starts_at=datetime.fromisoformat("2023-09-18 11:00:00+00"),
            duration=20,
        )
        expected_ends_at = datetime.fromisoformat("2023-09-18 11:19:59+00")
        self.assertEqual(reservation.ends_at, expected_ends_at)

    def test_reservation_created_when_available_after(self):
        reservation = Reservation.objects.create(
            car=self.car,
            starts_at=datetime.fromisoformat("2023-09-18 11:50:00+00"),
            duration=15,
        )
        expected_ends_at = datetime.fromisoformat("2023-09-18 12:04:59+00")
        self.assertEqual(reservation.ends_at, expected_ends_at)

    def test_reservation_not_created_when_overlaps(self):
        with self.assertRaises(exceptions.ValidationError):
            Reservation.objects.create(
            car=self.car,
                starts_at=datetime.fromisoformat("2023-09-18 10:00:00+00"),
                duration=30,
            )
        with self.assertRaises(exceptions.ValidationError):
            Reservation.objects.create(
            car=self.car,
                starts_at=datetime.fromisoformat("2023-09-18 10:50:00+00"),
                duration=30,
            )
