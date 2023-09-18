from django.db import models
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError
import re

class Car(models.Model):
    uid = models.CharField(db_column="id")
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    @property
    def uid(self):
        return f"C{self.id}"

    @classmethod
    def uid_to_id(cls, value):
        if value == None:
            return value

        match = re.search(r'^C(?P<id>\d+)$', value, re.IGNORECASE)
        if match:
            return match["id"]

        raise ValidationError(
            _("Invalid UID"),
            code="invalid",
            params={"field": "uid"},
        )

    @uid.setter
    def uid(self, value):
        self.id = self.__class__.uid_to_id(value)
