from pydantic import BaseModel, Field
from typing import List, Optional


class CandidateSummary(BaseModel):
    name: Optional[str] = None
    experience_years: Optional[int] = None
    skills: Optional[List[str]] = []
    summary: str


class ResumeEvaluation(BaseModel):
    score: int = Field(..., ge=1, le=10)
    strengths: List[str]
    weaknesses: List[str]
