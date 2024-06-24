from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from langflow.load import run_flow_from_json

# Define the FastAPI router
router = APIRouter()

# Pydantic model for the request body
class QuestionRequest(BaseModel):
    question: str

# Pydantic model for the response
class RunOutput(BaseModel):
    output: str

@router.post("/send-input-message", response_model=List[RunOutput])
async def process_flow(request: QuestionRequest):
    """
    Process the flow based on the input question and return the result.
    """
    try:
        result = run_flow_from_json(
            flow="../langflow/json_schemas/PDF RAG Search (with tables parsed).json",
            input_value=request.question,
            fallback_to_env_vars=True
        )

        # Convert result to response model
        response = [RunOutput(output=output) for output in result]
        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
