from fastapi import APIRouter
from app.services.agent_service import invoke_agent
from app.models.request import AgentRequest

router = APIRouter()

@router.post("/ask")
async def ask_agent(request: AgentRequest):
    """Handles AI agent queries."""
    response = invoke_agent(request.input)
    return {"response": response}
