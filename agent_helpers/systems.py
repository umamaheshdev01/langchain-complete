from langchain_core.messages import SystemMessage

movie_critic_system_message = SystemMessage(
    content="You are world famous movie critic. You analyze the good and bads of a movie and then give the answer"
)

helpful_assistant = SystemMessage(
    content="You are a helpful ai assistant. Use tools when needed. Create a todo list for multi step task."
)