import asyncio
import websockets
import redis

r=redis.Redis(host='10.10.71.11',
port=6379,
db=0)

async def hello(websocket, path):
    key = await websocket.recv()
    val = f"{r.get(key)}"
    await websocket.send(val)

start_server = websockets.serve(hello, '0.0.0.0', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
