import asyncio
import websockets

ip = "localhost"	
port = 8765

async def main():
    async with websockets.connect(f"ws://{ip}:{port}") as websocket:
        # Send a message to the server
        await websocket.send("Hello from the client!")
        # Receive a message from the server
        response = await websocket.recv()
        print(f"Received response: {response}")

if __name__ == "__main__":
    asyncio.run(main())