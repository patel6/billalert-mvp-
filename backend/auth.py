from fastapi import HTTPException, status
import uuid

# Global "Database" for the demo session
# Structure: { "session_id": { "username": "satya", "preferences": {} } }
active_sessions = {}

def create_session(username: str):
    session_id = str(uuid.uuid4())
    active_sessions[session_id] = {
        "username": username,
        "preferences": None,
        "history": []
    }
    return session_id

def get_session(session_id: str):
    if session_id not in active_sessions:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Session expired or invalid"
        )
    return active_sessions[session_id]