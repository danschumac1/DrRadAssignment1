import os
import openai
from dotenv import load_dotenv

def load_env():
    load_dotenv("./resources/.env")
    return os.getenv("OPENAI_API_KEY")

# Initialize OpenAI Client with API Key
CLIENT = openai.OpenAI(api_key=load_env())

def get_completion(system_message: str, prompt: str, model: str = "gpt-4o-mini") -> str:
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": prompt}
    ]
    
    response = CLIENT.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
        response_format={"type": "json_object" }  # Change to "json" if structured response is needed
    )

    return response.choices[0].message.content  # Fix incorrect access

def main():
    system_message = "You are a helpful assistant that is here to help the user with their tasks. Always answer in some json format"
    prompt = "What is the capital of the United States?"
    completion = get_completion(system_message, prompt)
    print(completion)

if __name__ == '__main__':
    main()
