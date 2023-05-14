from django.urls import path
from .consumers import BaseConsumer

ws_urlpatterns = [
    path('ws/base/', BaseConsumer.as_asgi())
]
