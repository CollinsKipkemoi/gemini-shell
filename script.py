import os
from dotenv import load_dotenv
import google.generativeai as genai
from datetime import datetime
import json


class GeminiShell:
    def __init__(self):
        load_dotenv()
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        self.model = genai.GenerativeModel("gemini-2.0-flash")
        self.history = []
        self.max_history = 10
        self.filename = f"chat_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    def chat(self):
        print("Welcome to Gemini Shell!")
        try:
            while True:
                try:
                    question = input("User: ")
                    response = self.model.generate_content(contents=question)
                    print(f"AI: {response.text}")
                except Exception as e:
                    print(f"An error occurred: {e}")
        except KeyboardInterrupt:
            print("Goodbye! Thanks for using Gemini Shell!")


if __name__ == "__main__":
    GeminiShell().chat()
