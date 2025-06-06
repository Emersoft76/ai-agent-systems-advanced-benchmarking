"""
Multimodal Task Runner
-----------------------

🚀 Purpose:
Handles complex tasks that require both visual and textual input, such as:
- Image analysis with follow-up questions
- OCR-to-reasoning pipelines
- Document routing and classification

📦 Requirements:
- openai >= 1.0.0
- python-dotenv
- requests
- Pillow

Usage:
$ python examples/multimodal_task_runner.py <image_path> "<instruction>"
"""

import os
import sys
from dotenv import load_dotenv
import requests
from PIL import Image
import base64
import mimetypes

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

headers = {
    "Authorization": f"Bearer {OPENAI_API_KEY}",
    "Content-Type": "application/json"
}

def encode_image(image_path):
    mime, _ = mimetypes.guess_type(image_path)
    with open(image_path, "rb") as img:
        encoded = base64.b64encode(img.read()).decode("utf-8")
    return f"data:{mime};base64,{encoded}"

def run_multimodal_pipeline(image_path, instruction):
    encoded_image = encode_image(image_path)

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": [
                    { "type": "text", "text": instruction },
                    {
                        "type": "image_url",
                        "image_url": { "url": encoded_image }
                    }
                ]
            }
        ],
        "max_tokens": 1000
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python multimodal_task_runner.py <image_path> '<instruction>'")
        sys.exit(1)

    result = run_multimodal_pipeline(sys.argv[1], sys.argv[2])
    print("\n🤖 Result:\n", result)
