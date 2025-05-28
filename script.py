import os
from dotenv import load_dotenv
import google.generativeai as genai
from datetime import datetime


class GeminiShell:
    def __init__(self):
        load_dotenv()
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        self.model = genai.GenerativeModel("gemini-2.0-flash")
        self.history = []

    def chat(self):
        print("Welcome to Gemini Shell!")
        try:
            while True:
                question = input("User: ")
                self.history.append({"role": "user", "parts": [question]})

                try:
                    response = self.model.generate_content(contents=self.history)
                    self.history.append({"role": "assistant", "parts": [response.text]})
                    print(f"AI: {response.text}")
                except Exception as e:
                    print(f"An error occurred: {e}")
        except KeyboardInterrupt:
            print("\nGoodbye! Thanks for using Gemini Shell!")


if __name__ == "__main__":
    GeminiShell().chat()
