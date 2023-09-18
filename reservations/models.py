from django.db import models
from datetime import datetime, timedelta

from cars.models import Car

class Reservation(models.Model):
    car = models.ForeignKey(Car, on_delete=models.RESTRICT)
    _starts_at = models.DateTimeField(db_column="starts_at", db_comment="minutes precision")
    duration = models.PositiveIntegerField(db_comment="in minutes")

    @classmethod
    def down_to_minute(cls, value=None):
        if not value:
            value = datetime.now()
        value = value.replace(second=0, microsecond=0)
        return value

    @property
    def starts_at(self):
        return self.down_to_minute(self._starts_at)

    @starts_at.setter
    def starts_at(self, value):
        self._starts_at = self.down_to_minute(value)

    @property
    def duraton_timedelta(self):
        return timedelta(minutes=self.duration, seconds=-1)

    @property
    def ends_at(self):
        """
        to get last second of the last minute
        """

        if not self.starts_at:
            return None
        if self.duration == 0:
            return None

        return self.starts_at + self.duraton_timedelta

    @classmethod
    def find_overlapped(cls, car_id, starts_at, duration):
        cls.objects.raw(
            """SQL
            SELECT
                id,
                car_id,
                starts_at,
                duration,
                DATE_ADD(starts_at, INTERVAL duration -1 MINUTE_SECOND) AS ends_at
            FROM
                reservations_reservation
            WHERE
                car_id = %s
            AND
                %s <= ends_at
            AND
                %s >= starts_at
            """,
            [
                car_id,
                starts_at,
                ends_at,
            ]
        )
