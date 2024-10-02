import os
import requests
import base64
from dotenv import load_dotenv

# Note: This module is designed to work with the OpenAI GPT-4O API for processing text and images. 
# The decision to use GPT-4O is due to the requirement of using an open source model, but the inability to run any model locally. 
# GPT-4O is chosen as it provides a similar functionality to open source LLMs like LLama 3.2 multi-model ones
# ensuring a comparable performance without the need for local model deployment.

load_dotenv()

def process_image_and_text(text: str, image_path: str) -> dict:
    """
    This function processes the given text and image by sending them to the OpenAI GPT-4O API for processing.
    The image is first encoded in base64 format and then sent along with the text to the API.
    The API is configured to use a system message that instructs the model to correct any mistakes in the text retrieved from OCR.
    The function returns the JSON response from the API.

    Parameters:
    - text (str): The text to be processed.
    - image_path (str): The path to the image file to be processed.

    Returns:
    - dict: The JSON response from the OpenAI GPT-4O API.
    """
    
    # Configuration
    API_KEY = os.getenv("OPENAI_API_KEY")
    ENDPOINT = os.getenv("OPENAI_API_ENDPOINT")
    
    # Encode image
    with open(image_path, 'rb') as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode('ascii')

    # Headers
    headers = {
        "Content-Type": "application/json",
        "api-key": API_KEY,
    }

    # Payload
    payload = {
        "messages": [
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": "The user will give Kannada text with an image. The text was retrieved from OCR. Your task is to read the content and fix any mistakes it makes. NOTE: dont add any extra data like here is your corrected text. the response should only be there."
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": text
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{encoded_image}"
                        }
                    }
                ]
            }
        ],
        "temperature": 0.7,
        "top_p": 0.95,
        "max_tokens": 4000,
    }

    # Send request
    try:
        response = requests.post(ENDPOINT, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise SystemExit(f"Failed to make the request. Error: {e}")
    