from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.deepseek import DeepSeekProvider
from dotenv import load_dotenv
import tools
import os

load_dotenv()

apiKey = os.getenv("OPENAI_API_KEY")
if not apiKey:
    raise ValueError("The environment variable 'OPENAI_API_KEY' is not set.")

model = OpenAIModel(
    'deepseek-chat',
    provider=DeepSeekProvider(api_key = apiKey),
)
agent = Agent(model,
              system_prompt='You are an experienced programmer.',
              tools=[tools.list_files,tools.read_file, tools.rename_file])

def main():
    history = []
    while True:
        user_input = input("Input: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Exiting the chat.")
            break
        response = agent.run_sync(user_input)
        history = list(response.all_messages())
        print(f"Agent: {response}")

if __name__ == "__main__":
    main()