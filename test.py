import os
import google.generativeai as genai
from google.generativeai import protos
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

tool = protos.Tool(google_search=protos.Tool.GoogleSearch())
model = genai.GenerativeModel(model_name="gemini-2.5-pro", tools=[tool])
response = model.generate_content("What is the weather in Tokyo today?")
print(response.text)
