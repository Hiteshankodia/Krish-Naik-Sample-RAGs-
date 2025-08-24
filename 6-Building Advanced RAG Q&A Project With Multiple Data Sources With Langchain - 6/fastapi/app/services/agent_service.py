from langchain import hub
from langchain.agents import create_openai_tools_agent, AgentExecutor
from app.utils.load_tools import TOOLS
from app.dependencies import llm

# Load the prompt template
prompt = hub.pull("hwchase17/openai-functions-agent")

# Create AI Agent
agent = create_openai_tools_agent(llm, TOOLS, prompt)

# Agent Executor
agent_executor = AgentExecutor(agent=agent, tools=TOOLS, verbose=True)

def invoke_agent(user_input: str):
    """Invoke the AI agent with a user input."""
    response = agent_executor.invoke({"input": user_input})
    return response
