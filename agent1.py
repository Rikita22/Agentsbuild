import logging
from datetime import datetime
from dotenv import load_dotenv

from agentspan.agents import Agent, AgentRuntime, ConversationMemory, run, tool

load_dotenv()
logging.basicConfig(level=logging.WARNING)
logging.getLogger("agentspan").setLevel(logging.WARNING)
logging.getLogger("agentspan").setLevel(logging.WARNING)

@tool
def get_current_time() -> str:
    """Returns the current time"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

conversation_memory = ConversationMemory(max_messages=50)

assistant = Agent(
    name="assistant",
    description="A helpful assistant that can answer questions and help with tasks",
    instructions=("You are a helpful assistant that can answer questions and help with tasks"),
    tools=[get_current_time],
    model="gpt-4o-mini",
    memory=conversation_memory,
    max_tokens=1000,
    temperature=0.0,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
)

if __name__ == "__main__":
    print("Starting agent1...")
    with AgentRuntime(assistant) as runtime:
        while True:
            prompt = input("Enter a prompt: ")
            if prompt.lower() == "exit":
                break
            result = run(assistant,prompt,runtime=runtime)  
            conversation_memory.add_user_message(prompt)
            conversation_memory.add_assistant_message(result.output.get('result'))
            print(f"Assistant:{result.output.get('result')}")