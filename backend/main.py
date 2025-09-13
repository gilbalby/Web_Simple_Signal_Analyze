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
    
        # 🚨 Casos especiais
    # 1) Sinal com apenas um valor
    if len(signal) == 1:
        trend = "estável"
    # 2) Todos os valores são iguais
    elif np.all(signal == signal[0]):
        trend = "estável"
    else:
        # Divide em duas metades para análise de tendência
        first_half = signal[:len(signal)//2]
        second_half = signal[len(signal)//2:]

        first_mean = np.mean(first_half)
        second_mean = np.mean(second_half)

        # Verifica variação relativa
        if np.mean(signal) == 0:
            # Se a média global for zero mas não são todos iguais, tendência depende do início/fim
            trend = "crescente" if second_mean > first_mean else "decrescente"
        elif abs(second_mean - first_mean) < 0.1 * abs(np.mean(signal)):  # tolerância de 10%
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