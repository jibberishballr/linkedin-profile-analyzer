from fastapi import FastAPI
import modal

from pydantic import BaseModel
from sklearn.linear_model import LogisticRegression
import numpy as np
import requests
from fastapi.middleware.cors import CORSMiddleware



secret = modal.Secret.from_name("hunter-api-key")

app = FastAPI()

origins = [
    "https://www.linkedin.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Sample data for training the model
# In a real application, this would be a much larger and more comprehensive dataset.
X_train = np.array([[2, 1], [8, 7], [1, 1], [9, 8], [3, 2], [7, 6]])
y_train = np.array([0, 1, 0, 1, 0, 1])

# Train a simple logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

class ProfileData(BaseModel):
    name: str
    title: str
    company: str
    experience: list



def get_verified_email(name: str, company: str, api_key: str):
    url = f"https://api.hunter.io/v2/email-finder?company={company}&full_name={name}&api_key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data.get("data") and data["data"].get("email"):
            return data["data"]["email"]
    return "Email not found"

@app.post("/analyze")
async def analyze_profile(data: ProfileData):
    # Extract features from the profile data
    # This is a simplified example. A real application would use more sophisticated feature engineering.
    features = np.array([[len(data.experience), len(data.title)]])

    # Predict the connection probability
    connection_probability = model.predict_proba(features)[0][1]

    # Get the verified email address
    email = get_verified_email(data.name, data.company, api_key)

    contact_info = {
        "email": email,
        "phone": "123-456-7890"  # Placeholder for phone number
    }

    try:
        api_key = secret["HUNTER_API_KEY"]
    except modal.exception.NotFoundError:
        email = "Hunter API key not found in Modal secrets."
        api_key = None # Set api_key to None if not found

    return {
        "connection_probability": connection_probability,
        "contact_info": contact_info
    }

@app.get("/")
async def root():
    return {"message": "LinkedIn Profile Analyzer backend is running."}
