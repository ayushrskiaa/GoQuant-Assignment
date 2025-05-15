import asyncio
import websockets
import json
import logging
import time

class OrderBookWebSocket:
    def __init__(self, url, symbol, on_tick, reconnect_delay=5):
        self.url = url
        self.symbol = symbol
        self.on_tick = on_tick
        self.reconnect_delay = reconnect_delay

    async def connect(self):
        while True:
            try:
                async with websockets.connect(self.url) as ws:
                    logging.info(f"Connected to {self.url}")
                    async for message in ws:
                        start = time.perf_counter()
                        data = json.loads(message)
                        await self.on_tick(data, time.perf_counter() - start)
            except Exception as e:
                logging.error(f"WebSocket error: {e}. Reconnecting in {self.reconnect_delay} seconds...")
                await asyncio.sleep(self.reconnect_delay)