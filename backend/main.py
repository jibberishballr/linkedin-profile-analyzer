from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ProfileData(BaseModel):
    name: str
    title: str
    company: str
    experience: list

@app.post("/analyze")
async def analyze_profile(data: ProfileData):
    # Placeholder for connection probability logic
    connection_probability = 0.85  # Example value

    # Placeholder for contact info verification
    contact_info = {
        "email": "example@example.com",
        "phone": "123-456-7890"
    }

    return {
        "connection_probability": connection_probability,
        "contact_info": contact_info
    }

@app.get("/")
async def root():
    return {"message": "LinkedIn Profile Analyzer backend is running."}
