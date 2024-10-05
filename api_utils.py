import os
from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel

# Load environment variables from .env file
load_dotenv()

class ResponseFormat(BaseModel):
    message: str
    OpenScadCode: str

def openai_api_call(text_input):
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("OpenAI API key is not set. Please set the OPENAI_API_KEY environment variable.")

    # Initialize OpenAI client
    client = OpenAI(api_key=api_key)

    try:
        # Create a chat completion using the client instance
        completion = client.beta.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            messages=[
                {"role": "system", "content": "You are a CAD agent that takes a user request and responds with a message object and executable OpenSCAD code."},
                {"role": "user", "content": text_input}
            ],
            response_format=ResponseFormat
        )

        # Extract the assistant's reply
        assistant_reply = completion.choices[0].message
        if assistant_reply.parsed:
            # Print message and return OpenScad Code
            print("Message:")
            print(assistant_reply.parsed.message)
            return assistant_reply.parsed.OpenScadCode
        elif assistant_reply.refusal:
            # Handle refusal
            print("Refusal:")
            print(assistant_reply.refusal)
    except OpenAI.LengthFinishReasonError as e:
        # Retry with a higher max tokens or handle accordingly
        print("Too many tokens:", e)
    except Exception as e:
        # Handle other exceptions
        print(f"[ERROR] An error occurred: {e}")
