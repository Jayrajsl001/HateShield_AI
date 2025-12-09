# app/models.py
from pydantic import BaseModel, Field
from typing import Optional, List

class AnalyzeRequest(BaseModel):
    text: str = Field(..., min_length=1, description="Text to analyze")
    language: str = Field("auto", description="Language code or 'auto'")

class AnalysisResult(BaseModel):
    is_hate: bool
    category: str
    severity: float
    language: str
    confidence: float
    explanation: Optional[str] = None

class AnalyzeResponse(BaseModel):
    result: AnalysisResult

class BulkItemResult(BaseModel):
    id: int
    text: str
    result: AnalysisResult

class BulkAnalyzeRequest(BaseModel):
    texts: List[str]
    language: str = "auto"

class BulkAnalyzeResponse(BaseModel):
    results: List[BulkItemResult]
