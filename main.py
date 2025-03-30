from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from agents.clinical_agent import ClinicalAgent
from agents.food_security_agent import FoodSecurityAgent

app = FastAPI()

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize agents
clinical_agent = ClinicalAgent([
    "Clinical data placeholder",
    "Medical studies on diabetes",
    "Latest cancer research findings"
])
food_security_agent = FoodSecurityAgent([
    "Food Security data placeholder",
    "Global hunger statistics from 2024",
    "Nutritional guidelines for developing countries"
])

class Query(BaseModel):
    question: str

@app.get("/")
async def root():
    return {"message": "Welcome to WebUI Copilots API"}

@app.post("/clinical")
async def clinical_query(data: Query):
    try:
        response = clinical_agent.query(data.question)
        return {"response": response}
    except Exception as e:
        return {"error": str(e)}

@app.post("/food_security")
async def food_security_query(data: Query):
    try:
        response = food_security_agent.query(data.question)
        return {"response": response}
    except Exception as e:
        return {"error": str(e)}
