from django.db import models
from datetime import datetime

from cars.models import Car

class Reservation(models.Model):
    car = models.ForeignKey(Car, on_delete=models.RESTRICT)
    starts_at = models.DateTimeField(db_comment="minutes precision")
    duration = models.PositiveIntegerField(db_comment="in minutes")

    @classmethod
    def down_to_minute(cls, value=None):
        if not value:
            value = datetime.now()
        value = value.replace(second=0, microsecond=0)
        return value

    @property
    def ends_at(self):
        """
        to get last second of the last minute
        """

        if not self.starts_at:
            return None
        if self.duration == 0:
            return None

        return self.down_to_minute(self.starts_at) + self.duration * 60 - 1
