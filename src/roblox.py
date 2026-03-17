import asyncio
import threading
import keyboard
import websockets
from websockets import WebSocketServerProtocol

from config import WEBSOCKET_PORT
from src.logger.logger import setup_logger
from src.utils import set_console_title

logger = setup_logger()

class RobloxWebsocket:
    def __init__(self):
        self.connected_clients = set()
        self._paused = False
        self._lock = threading.Lock()

    @property
    def paused(self):
        with self._lock:
            return self._paused

    async def handler(self, websocket: WebSocketServerProtocol):
        logger.info(f"> New client: {websocket.remote_address}")
        self.connected_clients.add(websocket)

        try:
            await asyncio.Future()
        finally:
            self.connected_clients.remove(websocket)

    async def broadcast(self, message: str):
        if self.paused:
            return

        dead_clients = set()

        for client in self.connected_clients:
            try:
                await client.send(message)
            except websockets.ConnectionClosed:
                dead_clients.add(client)

        if dead_clients:
            self.connected_clients.difference_update(dead_clients)


    async def run(self):
        async with websockets.serve(self.handler, "127.0.0.1", WEBSOCKET_PORT):
            logger.info(f"> Websocket server started: ws://127.0.0.1:{WEBSOCKET_PORT}")
            await asyncio.Future()


    def toggle_pause(self):
        with self._lock:
            self._paused = not self._paused
            new_paused = self._paused

        status_text = "Pause" if new_paused else "Enabled"
        logger.info(
            "> The script is paused (F2 button)"
            if new_paused else "> The script continued to run. (F2 button)"
        )
        set_console_title(f"AutoJoiner | Status: {status_text}")

    def keybrd_listener(self):
        keyboard.add_hotkey('F2', self.toggle_pause)
        keyboard.wait()


server = RobloxWebsocket()
def roblox_main():
    threading.Thread(target=server.keybrd_listener, daemon=True).start()
    asyncio.run(server.run())

# https://github.com/claay-rip/roblox-autojoiner