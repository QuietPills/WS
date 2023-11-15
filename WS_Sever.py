import asyncio
import sys
from websockets.server import serve

# ip_addr = sys.argv[1]

# if ip_addr.replace(" ","") == "":
#     ip_addr = "localhost"


async def echo(websocket):
    async for message in websocket:
        print("Message Recived")
        await websocket.send(str(message) + "aa")

async def main():
    # print(localhost + ":" + str(8765))
    async with serve(echo, "0.0.0.0", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())