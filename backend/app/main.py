# app/main.py

import logging
from fastapi import FastAPI, HTTPException


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import API_TITLE, API_VERSION
from .models import (
    AnalyzeRequest,
    AnalyzeResponse,
    BulkAnalyzeRequest,
    BulkAnalyzeResponse,
    BulkItemResult,
    AnalysisResult,
)
from .ml_model import predict_single

app = FastAPI(title=API_TITLE, version=API_VERSION)

# Allow frontend (Vite default: http://localhost:5173)
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "HateShield AI API is running"}

@app.post("/analyze", response_model=AnalyzeResponse)
def analyze_text(payload: AnalyzeRequest):
    try:
        pred = predict_single(payload.text, payload.language)
        result = AnalysisResult(**pred)
        return AnalyzeResponse(result=result)
    except Exception as e:
        logging.exception("Error during prediction")
        # This will return a JSON 500 instead of plain "Internal Server Error"
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/analyze/bulk", response_model=BulkAnalyzeResponse)
def analyze_bulk(payload: BulkAnalyzeRequest):
    results = []
    for idx, text in enumerate(payload.texts):
        pred = predict_single(text, payload.language)
        result = AnalysisResult(**pred)
        results.append(
            BulkItemResult(
                id=idx,
                text=text,
                result=result
            )
        )
    return BulkAnalyzeResponse(results=results)
