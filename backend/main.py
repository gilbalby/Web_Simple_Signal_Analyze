from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import numpy as np

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SignalRequest(BaseModel):
    signal: List[float]

class SignalResponse(BaseModel):
    mean: float
    min: float
    max: float
    trend: str

@app.post("/analyze", response_model=SignalResponse)
async def analyze_signal(request: SignalRequest):
    if not request.signal:
        raise HTTPException(status_code=400, detail="Signal array is empty")
    
    signal = np.array(request.signal)
    
    # Calculate basic statistics
    mean_value = float(np.mean(signal))
    min_value = float(np.min(signal))
    max_value = float(np.max(signal))
    
    # 1) Signal with single value
    if len(signal) == 1:
        trend = "estável"
    # 2) Signal with all different values
    elif np.all(signal == signal[0]):
        trend = "estável"
    else:
        # Split signal to trend
        first_half = signal[:len(signal)//2]
        second_half = signal[len(signal)//2:]

        first_mean = np.mean(first_half)
        second_mean = np.mean(second_half)

        # Check variation
        if np.mean(signal) == 0:
            # If the global average is zero, but not all are the same, the trend depends on the start/end
            trend = "crescente" if second_mean > first_mean else "decrescente"
        elif abs(second_mean - first_mean) < 0.1 * abs(np.mean(signal)):  # threshold 10%
            trend = "estável"
        elif second_mean > first_mean:
            trend = "crescente"
        else:
            trend = "decrescente"

    return SignalResponse(
        mean=mean_value,
        min=min_value,
        max=max_value,
        trend=trend
    )