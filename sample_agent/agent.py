from google.adk.agents import LlmAgent as Agent
from google.adk.tools.agent_tool import AgentTool
from .sub_agents.time import time_agent
from .sub_agents.weather import weather_agent

root_agent = Agent(
    name="weather_time_agent",
    model="gemini-2.0-flash-lite",
    description=(
        "Agent to answer questions about the details of a city."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about the details of a city. List of details present for a city is just time and weather for now, we will add to the list whenever possible. If details of a city are asked - just return both the time and weather. Hide the date, just show the time."
    ),
    tools=[
        AgentTool(agent=weather_agent),
        AgentTool(agent=time_agent),
        ],
)