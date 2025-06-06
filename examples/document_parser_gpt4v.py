"""
Document Parser with GPT-4 Vision
----------------------------------

📌 Purpose:
Parses and extracts structured content from visual documents (e.g., receipts, invoices, ID cards).

📦 Requirements:
- openai >= 1.0.0
- python-dotenv
- PIL (Pillow)
- requests

Usage:
$ python examples/document_parser_gpt4v.py <path_to_image_or_pdf>
"""

import os
import sys
from dotenv import load_dotenv
import requests
from PIL import Image
import base64
import mimetypes

# Load environment
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Define headers for API call
headers = {
    "Authorization": f"Bearer {OPENAI_API_KEY}",
    "Content-Type": "application/json"
}

def encode_image_to_base64(image_path):
    mime_type, _ = mimetypes.guess_type(image_path)
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode("utf-8")
    return f"data:{mime_type};base64,{encoded}"

def gpt4v_parse_image(image_path):
    image_data = encode_image_to_base64(image_path)

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": [
                    { "type": "text", "text": "Extract key information from this document and present it as structured JSON." },
                    {
                        "type": "image_url",
                        "image_url": { "url": image_data }
                    }
                ]
            }
        ],
        "max_tokens": 1000
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

# CLI Execution
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python document_parser_gpt4v.py <image_path>")
        sys.exit(1)

    result = gpt4v_parse_image(sys.argv[1])
    print("\n📄 Parsed Output:\n", result)
