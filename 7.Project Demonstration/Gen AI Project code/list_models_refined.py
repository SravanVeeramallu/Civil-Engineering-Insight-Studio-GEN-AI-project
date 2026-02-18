import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("No key found")
    exit()

url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"
try:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        models = [m['name'] for m in data.get('models', [])]
        print(f"Total models found: {len(models)}")
        
        # Check for specific models
        flash_1_5 = next((m for m in models if 'gemini-1.5-flash' in m), None)
        pro_1_5 = next((m for m in models if 'gemini-1.5-pro' in m), None)
        flash_2_0 = next((m for m in models if 'gemini-2.0-flash' in m), None)

        if flash_1_5: print(f"FOUND: {flash_1_5}")
        if pro_1_5: print(f"FOUND: {pro_1_5}")
        if flash_2_0: print(f"FOUND: {flash_2_0}")

        print("\nAll models:")
        for m in models:
            print(m)
            
    else:
        print(f"Error: {response.status_code} - {response.text}")
except Exception as e:
    print(f"Exception: {e}")
