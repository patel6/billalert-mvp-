from fastapi import FastAPI, Depends, Header
from fastapi.middleware.cors import CORSMiddleware
from .models import UserLogin, UserPreferences
from .auth import create_session, get_session
import os
from dotenv import load_dotenv

# This loads the keys from .env into your system's memory
load_dotenv()

GEMINI_KEY = os.getenv("OPENAI_API_KEY")
OPENSTATES_KEY = os.getenv("OPENSTATES_API_KEY")
app = FastAPI(title="BillAlert API")

# Enable CORS for Lilith's React/Vite frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], # Standard Vite port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/auth/login")
async def login(user: UserLogin):
    # SIMPLE DEMO CHECK: Accept any password for the demo
    if user.username and user.password:
        session_id = create_session(user.username)
        return {"session_id": session_id, "message": "Login successful"}
    raise HTTPException(status_code=400, detail="Invalid credentials")

@app.post("/user/preferences")
async def save_preferences(
    prefs: UserPreferences, 
    session_id: str = Header(...)
):
    session = get_session(session_id)
    session["preferences"] = prefs
    return {"message": "Preferences updated"}

@app.get("/health")
def health_check():
    return {"status": "online", "env": "Arizona-MVP"}
from .services.bill_service import fetch_az_bills

@app.post("/bills/summarize")
async def get_summary(bill: Bill, session_id: str = Header(...)):
    # Verify the session exists in our in-memory store
    get_session(session_id)
    
    # Generate summary
    summary = await summarize_bill(bill.title, bill.full_text_url)
    
    return {
        "bill_id": bill.bill_id,
        "summary": summary,
        "engine": "GPT 5.0"
    }