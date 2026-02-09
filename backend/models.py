from pydantic import BaseModel, Field
from typing import List, Optional

# 1. For user login
class UserLogin(BaseModel):
    username: str
    password: str

# 2. For preference selection
class UserPreferences(BaseModel):
    categories: List[str]  # e.g., ["Healthcare", "Finance"]
    days_back: int = Field(default=7, ge=1, le=30) # Arizona bills from last X days

# 3. For the Bill data (matches OpenStates/LegiScan structure)
class Bill(BaseModel):
    bill_id: str
    title: str
    category: str
    summary: Optional[str] = None  # This will be populated by Claude
    full_text_url: str