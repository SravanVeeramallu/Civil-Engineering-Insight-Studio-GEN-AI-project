import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
print(f"Using API Key: {api_key[:5]}...{api_key[-5:] if api_key else 'None'}")

if not api_key:
    print("API Key not found")
else:
    genai.configure(api_key=api_key)
    try:
        print("Listing models...")
        for m in genai.list_models():
            print(f"- {m.name}")
    except Exception as e:
        print(f"Error: {e}")
