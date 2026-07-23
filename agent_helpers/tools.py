from langchain.tools import tool
from agent_helpers.structures import WeatherInput


@tool("search_user",description="Tool used for searching information of a person")
def search_about_user(name: str) -> str:
    """Search for information about the user mentioned"""
    return f"The user {name} is a handsome guy"


@tool("get_weather",description="Get current weather and optional forecast of a location",args_schema=WeatherInput)
def get_weather(location: str, units: str = "celsius", include_forecast: bool = False) -> str:
    """Get current weather and optional forecast."""
    temp = 22 if units == "celsius" else 72
    result = f"Current weather in {location}: {temp} degrees {units[0].upper()}"
    if include_forecast:
        result += "\nNext 5 days: Sunny"
    return result