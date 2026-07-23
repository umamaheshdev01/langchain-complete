from dotenv import load_dotenv
from langchain.agents import create_agent
load_dotenv(override=True)  
import os
os.environ.pop("OPENAI_BASE_URL", None)  
from agent_helpers.model import model
from agent_helpers.structures import Movie
from agent_helpers.systems import helpful_assistant
from agent_helpers.tools import get_weather
from agent_helpers.middleware import file_sys_per_middleware,summary_middlware,skills_middleware,memory_middleware
from agent_helpers.middleware import protection_middleware,humanloop_middlware

agent = create_agent(
    model=model,
    tools=[get_weather],
    system_prompt=helpful_assistant,
    # response_format=Movie,
    middleware=[humanloop_middlware,file_sys_per_middleware]
)
