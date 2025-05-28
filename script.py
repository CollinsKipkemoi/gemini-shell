from google import genai
from dotenv import load_dotenv
import os


def load_env():
    load_dotenv()
    API_KEY = os.getenv("GEMINI_API_KEY")
    return API_KEY


def main():
    client = genai.Client(api_key=load_env())
    print("Welcome to Gemini Shell!")
    while True:
        try:
            question = input("User: ")
            response = client.models.generate_content(
                model="gemini-2.0-flash", contents=question
            )
            print(f"AI: {response.text}")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
