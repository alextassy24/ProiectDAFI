from channels.generic.websocket import AsyncWebsocketConsumer
from random import randint
import json
from .models import Temperature
from asyncio import sleep


class BaseConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)

        temp_min_val = float(data['tempMinVal'])
        temp_max_val = float(data['tempMaxVal'])
        press_min_val = float(data['pressMinVal'])
        press_max_val = float(data['pressMaxVal'])

        for i in range(1000):
            await self.send(json.dumps({'i': i, 'value_temp': randint(temp_min_val, temp_max_val), 'value_press': randint(press_min_val, press_max_val)}))
            await sleep(3)

        await self.send(json.dumps({
            'tempMinVal': temp_min_val,
            'tempMaxVal': temp_max_val,
            'pressMinVal': press_min_val,
            'pressMaxVal': press_max_val
        }))
