from django.db import models
from django.contrib.auth.models import User


class Temperature(models.Model):
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.value} at {self.timestamp} for user {self.user}"


class Pressure(models.Model):
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.value} at {self.timestamp} for user {self.user}"
