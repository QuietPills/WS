from websockets.sync.client import connect

def hello():
    with connect("ws://136.244.78.99:8765") as websocket:
        websocket.send("Hello world!cl")
        message = websocket.recv()
        print(f"Received: {message}")

hello()