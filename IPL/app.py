from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from ai_model import ai_model

class InputData(BaseModel):
    date: int
    month: int
    crop: str
    district: str

app = FastAPI()

# Adding middleware for CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins for CORS
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def hello():
    return {"message": "HELLO WORLD"}

@app.post("/predict")
async def predict_price(item: InputData):
    # Validate crop type
    if item.crop not in ["Ragi", "Rice", "Onion", "Coconut", "Tomato"]:
        raise HTTPException(status_code=400, detail="Invalid crop type")
    
    # Validate district
    if item.district not in ["ba", "ch", "my", "tu", "ha"]:
        raise HTTPException(status_code=400, detail="Invalid district")
    
    # Validate date (1-31) and month (1-12)
    if not (1 <= item.date <= 31):
        raise HTTPException(status_code=400, detail="Invalid date. It should be between 1 and 31.")
    
    if not (1 <= item.month <= 12):
        raise HTTPException(status_code=400, detail="Invalid month. It should be between 1 and 12.")
    
    try:
        # Get the prediction result
        price = ai_model(item.date, item.month, item.crop, item.district)
        if not price:  # Handle case where model returns empty or invalid result
            raise HTTPException(status_code=500, detail="Model prediction failed.")
        
        return {"predicted_price": price[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")
