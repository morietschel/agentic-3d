import base64
import os

from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel

# Load environment variables from .env file
load_dotenv()


class ResponseFormat(BaseModel):
    message: str
    OpenScadCode: str


# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def openai_api_call(text_input):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError(
            "OpenAI API key is not set. Please set the OPENAI_API_KEY environment variable."
        )

    # Initialize OpenAI client
    client = OpenAI(api_key=api_key)

    try:
        # Create a chat completion using the client instance
        completion = client.beta.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            messages=[
                {
                    "role": "system",
                    "content": "You are a CAD agent that takes a user request and responds with a message object and executable OpenSCAD code. You only write CAD code to construct the object, never to render or display it.",
                },
                {"role": "user", "content": text_input},
            ],
            response_format=ResponseFormat,
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


def get_improved_openscad_code(openscad_code, description):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError(
            "OpenAI API key is not set. Please set the OPENAI_API_KEY environment variable."
        )

    # Initialize OpenAI client
    client = OpenAI(api_key=api_key)

    try:
        # Create a chat completion using the client instance
        completion = client.beta.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            messages=[
                {
                    "role": "system",
                    "content": "You are a CAD agent that takes a user request and responds with a message object and improved OpenSCAD code. You analyze the given OpenSCAD code and description of the target object, identify what is wrong with the code, and provide an improved version of the code. You do not render or display the object.",
                },
                {
                    "role": "user",
                    "content": f"Description: {description}\nOpenSCAD Code:\n{openscad_code}",
                },
            ],
            response_format=ResponseFormat,
        )

        # Extract the assistant's reply
        assistant_reply = completion.choices[0].message
        if assistant_reply.parsed:
            # Print message and return improved OpenScad Code
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
    return None


def get_error_based_on_image(openscad_image_path, description):
    base64_image = encode_image(openscad_image_path)

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError(
            "OpenAI API key is not set. Please set the OPENAI_API_KEY environment variable."
        )

    # Initialize OpenAI client
    client = OpenAI(api_key=api_key)

    try:
        # Create a chat completion using the client instance
        completion = client.beta.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "You are a CAD agent that takes a user request and responds with a message object and improved OpenSCAD code. You analyze the given OpenSCAD png file (image) and description of the target object, and identify what is wrong with the image.",
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            },
                        },
                    ],
                },
                {
                    "role": "system",
                    "content": f"Description: {description}\nImage Path:\n{openscad_image_path}",
                },
            ],
            response_format=ResponseFormat,
        )

        # Extract the assistant's reply
        assistant_reply = completion.choices[0].message
        if assistant_reply.parsed:
            # Print message and return improved OpenScad Code
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
    return None


# define dimension, always pass in permenent model.
# bad when it's floating


def get_improved_code_based_on_error(
    error_description, openscad_code, original_description
):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError(
            "OpenAI API key is not set. Please set the OPENAI_API_KEY environment variable."
        )

    # Initialize OpenAI client
    client = OpenAI(api_key=api_key)

    try:
        # Create a chat completion using the client instance
        completion = client.beta.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            messages=[
                {
                    "role": "system",
                    "content": "You are a CAD agent that takes a user request and responds with a message object and improved OpenSCAD code. You analyze the given error description, and original description of the target object, and return new openscad code that is improved based on fixing the errors in the error description.",
                },
                {
                    "role": "user",
                    "content": f"Description: {original_description}\nError: {error_description}\nNew OpenSCAD Code:\n{openscad_code}",
                },
            ],
            response_format=ResponseFormat,
        )

        # Extract the assistant's reply
        assistant_reply = completion.choices[0].message
        if assistant_reply.parsed:
            # Print message and return improved OpenScad Code
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
    return None
