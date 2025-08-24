from fastapi import FastAPI
from app.routes import agent

app = FastAPI(title="LangChain AI Agent API")

# Register Routes
app.include_router(agent.router, prefix="/agent", tags=["Agent"])

@app.get("/")
async def root():
    return {"message": "Welcome to the LangChain AI Agent API"}
