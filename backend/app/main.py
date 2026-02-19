from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import socketio
import os

load_dotenv()

app = FastAPI(
    title="WMAD AI Studio",
    description="Autonomous AI Workforce & Virtual Office Platform",
    version="1.0.0"
)

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change to your domain later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Socket.IO for real-time office
sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins="*")
socket_app = socketio.ASGIApp(sio, app)

@app.get("/")
async def root():
    return {
        "message": "🚀 WMAD AI Studio Backend is LIVE",
        "status": "healthy",
        "ceo": "Vijay Sekuru",
        "next": "Virtual Office + Atlas coming in next steps"
    }

@app.get("/health")
async def health():
    return {"status": "ok"}

# Socket.IO events (we will expand later)
@sio.event
async def connect(sid, environ):
    print(f"Agent or CEO connected: {sid}")
    await sio.emit("welcome", {"message": "Welcome to WMAD AI Studio, CEO Vijay!"})

@sio.event
async def disconnect(sid):
    print(f"Disconnected: {sid}")

# This allows docker to run it
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
