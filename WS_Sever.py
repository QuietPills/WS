import asyncio
import sys
from websockets.server import serve

async def echo(websocket):
    async for message in websocket:
        print(str(websocket.remote_address) + ":" +  str(message))
        await websocket.send(str(message))

async def main():
    async with serve(echo,"",8765):
        await asyncio.Future()  # run forever

asyncio.run(main())