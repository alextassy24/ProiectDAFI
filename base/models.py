from django.db import models
from django.contrib.auth.models import User


class Temperature(models.Model):
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.value} at {self.timestamp}"


class Pressure(models.Model):
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.value} at {self.timestamp}"
