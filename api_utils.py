import os
from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel
from config import SCENE_DESCRIPTION
import base64

# Load environment variables from .env file
load_dotenv()

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

class ResponseFormatCode(BaseModel):
    message: str
    OpenScadCode: str

class ResponseFormatFeedback(BaseModel):
    match: bool
    feedback: str

def initial_code_api_call():
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
                {"role": "system", "content": "You are a CAD agent that takes a user request and responds with a message object and executable OpenSCAD code. You only write CAD code to construct the object, never to render or display it."},
                {"role": "user", "content": "Give me the code for{SCENE_DESCRIPTION}."}
            ],
            response_format=ResponseFormatCode
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

def updated_code_api_call(current_scad_code, scene_feedback):
    """
    Calls the API to regenerate SCAD code based on feedback suggestions.
    """
     
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
                {
                    "role": "system",
                    "content": (
                        "You are a CAD agent. The user has provided feedback based on an image render. "
                        "Regenerate the SCAD code based on the suggestions for improvement."
                    )
                },
                {
                    "role": "user",
                    "content": (
                        f"Here is the current SCAD code: '{current_scad_code}'. The scene should depict '{SCENE_DESCRIPTION}'. "
                        f"Based on these suggestions: {scene_feedback}, please regenerate the SCAD code."
                    )
                }
            ], 
            response_format=ResponseFormatCode
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

def feedback_api_call(image_filepath):
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("OpenAI API key is not set. Please set the OPENAI_API_KEY environment variable.")

    # Initialize OpenAI client
    client = OpenAI(api_key=api_key)

    # Getting the base64 string
    base64_image = encode_image(image_filepath)


    try:
        # Create a chat completion for feedback using the client instance
        completion = client.beta.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an image feedback agent. Your role is to examine rendered images "
                        "and confirm whether they match the user’s intended description. Give an explicit boolean 'True' answer "
                        "if they do match. If they don't match, give an explicit boolean 'False' answer and "
                        "provide suggestions for how the scene can be improved."
                    )
                },
                {
                    "role": "user",
                    "content": [
                                    {
                                    "type": "text",
                                    "text": f"The image is attached. Here is the intended image description: {SCENE_DESCRIPTION}."
                                    },
                                    {
                                    "type": "image_url",
                                    "image_url": {
                                        "url":  f"data:image/jpeg;base64,{base64_image}"
                                    },
                                    },
                                ],
                }
            ], 
            response_format=ResponseFormatFeedback
        )

        # Extract the assistant's reply
        assistant_reply = completion.choices[0].message
        if assistant_reply.parsed:
            # Print message and return OpenScad Code
            print("Message:")
            print(assistant_reply.parsed.feedback)
            return {'match': assistant_reply.parsed.match, 'feedback': assistant_reply.parsed.feedback}
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