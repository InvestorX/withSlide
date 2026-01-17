import asyncio
import json
import logging
import websockets
import collections

# Configure logging
logging.basicConfig(level=logging.INFO)

# Rooms: roomId -> set(websocket)
rooms = collections.defaultdict(set)

async def signaling_handler(websocket):
    current_room = None
    try:
        async for message in websocket:
            try:
                data = json.loads(message)
                msg_type = data.get("type")

                if msg_type == "join":
                    room_id = data.get("roomId")
                    if room_id:
                        # Leave previous room if any
                        if current_room and websocket in rooms[current_room]:
                            rooms[current_room].remove(websocket)
                        
                        current_room = room_id
                        rooms[current_room].add(websocket)
                        logging.info(f"Client joined room: {room_id}")
                        # Notify join success or current peer count if needed (optional)
                
                elif msg_type in ["offer", "answer", "candidate", "request_offer"]:
                    # Relay to other peers in the room
                    if current_room:
                        target = data.get("target") # Optional: target specific peer if logic supports it
                        # Broadcast to all others in room
                        peers = rooms[current_room]
                        for peer in peers:
                            if peer != websocket:
                                await peer.send(message)
                        logging.info(f"Relayed {msg_type} in room {current_room}")
                
                elif msg_type == "ping":
                    await websocket.send(json.dumps({"type": "pong"}))

            except json.JSONDecodeError:
                logging.error("Invalid JSON")
            except Exception as e:
                logging.error(f"Error handling message: {e}")

    except websockets.exceptions.ConnectionClosed as e:
        logging.info("Client disconnected")
    finally:
        if current_room and websocket in rooms[current_room]:
            rooms[current_room].remove(websocket)
            if not rooms[current_room]:
                del rooms[current_room]

async def main():
    server = await websockets.serve(signaling_handler, "0.0.0.0", 8765)
    logging.info("Signaling server started on ws://0.0.0.0:8765 (accessible on local network)")
    await server.wait_closed()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
