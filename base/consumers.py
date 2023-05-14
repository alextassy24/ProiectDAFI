from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth.models import User
from .models import Temperature, Pressure
from random import randint
import json
from .models import Temperature
from asyncio import sleep


import asyncio


class BaseConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.status = None

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        action = data['action']
        temp_min_val = int(data['tempMinVal'])
        temp_max_val = int(data['tempMaxVal'])
        press_min_val = int(data['pressMinVal'])
        press_max_val = int(data['pressMaxVal'])
        print(action)

        if action == 'set':
            self.status = 'IDLE'
            await self.send(json.dumps({'status': self.status}))
            await asyncio.sleep(5)
            self.status = 'Heating'

            for i in range(temp_min_val, temp_max_val + 1):
                value_press = randint(press_min_val, press_max_val)
                await self.send(json.dumps({'i': i, 'value_press': value_press, 'value_temp': i, 'status': self.status}))

                await self.save_temperature(i)
                await self.save_pressure(value_press)

                await asyncio.sleep(3)

        elif action == 'cool':
            self.status = 'Cooling'
            await self.send(json.dumps({'status': self.status}))

        elif action == 'heat':
            self.status = 'Heating'
            await self.send(json.dumps({'status': self.status}))

        elif action == 'stop':
            self.status = 'Stop'
            await self.send(json.dumps({'status': self.status}))

    @database_sync_to_async
    def save_temperature(self, value):
        temperature = Temperature(value=value)
        temperature.save()

    @database_sync_to_async
    def save_pressure(self, value):
        pressure = Pressure(value=value)
        pressure.save()
