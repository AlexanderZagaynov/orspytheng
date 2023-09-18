from django.test import TestCase
from django.core import exceptions

from .models import Car

class CarTestCase(TestCase):

    def test_car_created_when_uid_correct(self):
        car = Car.objects.create(
            uid="C111",
            make="FirstMake",
            model="FirstModel",
        )
        self.assertEqual(car.id, 111)

    def test_car_not_created_when_uid_incorrect(self):
        with self.assertRaises(exceptions.ValidationError):
            Car.objects.create(
                uid="abc123",
                make="FirstMake",
                model="FirstModel",
            )

    def test_car_created_without_uid(self):
        car = Car.objects.create(
            make="FirstMake",
            model="FirstModel",
        )
        self.assertRegexpMatches(car.uid, r'^C\d+$')
