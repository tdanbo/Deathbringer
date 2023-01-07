import asyncio
import websockets

ip = "localhost"
port = 8765

async def handler(websocket):
    async for message in websocket:
        print(f"Received message: {message}")
        response = message + " from the server!"
        await websocket.send(f"Echo: {response}")

async def main():
    server = await websockets.serve(handler, ip, port)
    await server.wait_closed()

if __name__ == "__main__":
    print(f"Starting server on {ip}:{port}...")
    asyncio.run(main())