import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
print(f"Key: {api_key[:5]}...")

if not api_key:
    print("No API Key found.")
else:
    genai.configure(api_key=api_key)
    print("\n--- Listing Models ---")
    try:
        found_any = False
        for m in genai.list_models():
            found_any = True
            print(f"Model: {m.name}")
            print(f"Methods: {m.supported_generation_methods}")
        if not found_any:
            print("No models found. Check if API is enabled.")
    except Exception as e:
        print(f"Error listing models: {e}")

    print("\n--- Testing Generation (gemini-pro) ---")
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content("Hello")
        print(f"Response: {response.text}")
    except Exception as e:
        print(f"gemini-pro failed: {e}")
