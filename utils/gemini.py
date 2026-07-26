import os

import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()


class GeminiAdvisor:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY was not found in the .env file."
            )

        genai.configure(api_key=api_key)

        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def generate_response(self, prompt: str) -> str:
        response = self.model.generate_content(prompt)
        return response.text