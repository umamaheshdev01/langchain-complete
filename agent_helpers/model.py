from langchain.chat_models import init_chat_model

model = init_chat_model(
    model="gpt-5-nano",
    max_retries=10,
    timeout=120,
    reasoning_effort="low", 
    max_tokens=16000,  
)