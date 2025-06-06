import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent


def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city.

    Args:
        city (str): The name of the city for which to retrieve the current time.

    Returns:
        dict: status and result or error msg.
    """

    if city.lower() == "new york":
        tz_identifier = "America/New_York"
    else:
        return {
            "status": "error",
            "error_message": (
                f"Sorry, I don't have timezone information for {city}."
            ),
        }

    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    report = (
        f'The current time in {city} is {now.strftime("%Y-%m-%d %H:%M:%S %Z%z")}'
    )
    return {"status": "success", "report": report}


time_agent = Agent(
    name="time_agent",
    model="gemini-2.0-flash-lite",
    description=(
        "Agent to answer questions about the time in a city."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about the time in a city."
    ),
    tools=[get_current_time],
    output_key="report",
)