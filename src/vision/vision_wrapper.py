"""
Vision Wrapper
---------------

Provides a modular interface for handling visual input and integrating
with multimodal AI models (e.g. GPT-4V, Claude Vision).

✅ Responsibilities:
- Image parsing and pre-processing
- OCR and document understanding
- API interfacing for multimodal reasoning

"""

from PIL import Image
import pytesseract
import io
import base64
from typing import Optional

class VisionProcessor:
    def __init__(self, ocr_lang: str = "eng"):
        self.ocr_lang = ocr_lang

    def load_image(self, path: str) -> Image.Image:
        """Loads an image from disk."""
        return Image.open(path)

    def image_to_text(self, image: Image.Image) -> str:
        """Extracts text using OCR."""
        return pytesseract.image_to_string(image, lang=self.ocr_lang)

    def base64_to_image(self, base64_string: str) -> Image.Image:
        """Decodes base64 image to PIL."""
        image_data = base64.b64decode(base64_string)
        return Image.open(io.BytesIO(image_data))

    def process_document_image(self, path: str) -> str:
        """End-to-end processing from image path to extracted text."""
        image = self.load_image(path)
        return self.image_to_text(image)


# Example usage
if __name__ == "__main__":
    vp = VisionProcessor()
    result = vp.process_document_image("sample_invoice.png")
    print("📄 Extracted Text:\n", result)
