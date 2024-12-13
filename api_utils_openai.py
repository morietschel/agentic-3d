import os
from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel
import base64

# Load environment variables from .env file
load_dotenv()
CACHE_DB = ".cache/41/cache.db"

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

class ResponseFormatCode(BaseModel):
    message: str
    OpenScadCode: str

class ResponseFormatFeedback(BaseModel):
    feedback: str

class ResponseFormatTest(BaseModel):
    rating: int

def initial_code_api_call(scene_description):
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
                {"role": "system", "content": "You are a CAD agent that takes a user request and responds with a message object and executable OpenSCAD code. \
                                               You only write CAD code to construct the object, never to render or display it."
                },
                {"role": "user", "content": f"Give me the code for{scene_description}."}
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

def updated_code_api_call(scene_description, current_scad_code, scene_feedback):
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
                        f"Here is the current SCAD code: '{current_scad_code}'. The scene should depict{scene_description}. "
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
            print(f"Message: {assistant_reply.parsed.message}")
            return assistant_reply.parsed.OpenScadCode
        
        elif assistant_reply.refusal:
            # Handle refusal
            print(f"Refusal: {assistant_reply.refusal}")

    except OpenAI.LengthFinishReasonError as e:
        # Retry with a higher max tokens or handle accordingly
        print("Too many tokens:", e)

    except Exception as e:
        # Handle other exceptions
        print(f"[ERROR] An error occurred: {e}")

def feedback_api_call(scene_description, image_filepath):
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("OpenAI API key is not set. Please set the OPENAI_API_KEY environment variable.")

    # Initialize OpenAI client
    client = OpenAI(api_key=api_key)

    # Getting the base64 string
    print("image_filepath: " + image_filepath)
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
                        "and confirm whether they match the user’s intended description. "
                        "If they do match, explicitly say so and that the OpenSCAD code should stay the same. "
                        "If they do not match, explicitly say so and provide suggestions for how the scene can be improved."
                    )
                },
                {
                    "role": "user",
                    "content": [
                                    {
                                    "type": "text",
                                    "text": f"The image is attached. Here is the intended image description:{scene_description}."
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
            print(f"Feedback: {assistant_reply.parsed.feedback}")
            return {'feedback': assistant_reply.parsed.feedback}
        elif assistant_reply.refusal:
            # Handle refusal
            print(f"Refusal: {assistant_reply.refusal}")

    except OpenAI.LengthFinishReasonError as e:
        # Retry with a higher max tokens or handle accordingly
        print("Too many tokens:", e)

    except Exception as e:
        # Handle other exceptions
        print(f"[ERROR] An error occurred: {e}")

def test_api_call(scene_description, image_filepath):
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("OpenAI API key is not set. Please set the OPENAI_API_KEY environment variable.")

    # Initialize OpenAI client
    client = OpenAI(api_key=api_key)

    # Getting the base64 string
    print("image_filepath: " + image_filepath)
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
                        "and rate them on a scale of 1 to 10 for how well "
                        "each rendered image represents the intended description. A rating of 1 means the render DOES NOT match the "
                        "scene description and is very poor. A rating of 5 means the render DOES match the intended scene description "
                        "but it is not very good. A rating of 10 means the render perfectly matches the intended scene description and "
                        "the render does not need to be altered at all."
                    )
                },
                {
                    "role": "user",
                    "content": [
                                    {
                                    "type": "text",
                                    "text": f"The image is attached. Here is the intended image description:{scene_description}."
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
            response_format=ResponseFormatTest
        )

        # Extract the assistant's reply
        assistant_reply = completion.choices[0].message
        if assistant_reply.parsed:
            # Print message and return OpenScad Code
            print(f"Rating: {assistant_reply.parsed.rating}")
            return {'rating': assistant_reply.parsed.rating}
        elif assistant_reply.refusal:
            # Handle refusal
            print(f"Refusal: {assistant_reply.refusal}")

    except OpenAI.LengthFinishReasonError as e:
        # Retry with a higher max tokens or handle accordingly
        print("Too many tokens:", e)

    except Exception as e:
        # Handle other exceptions
        print(f"[ERROR] An error occurred: {e}")
        
def remove_cache():
    """
    Remove the cache database Autogen creates.
    """
    print("[DEBUG] Removing cache database.")
    os.remove(CACHE_DB)
    print("[DEBUG] Cache database removed successfully.")