import google.generativeai as genai
import os

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")
try:
    response = model.generate_content("안녕!")
    print("응답:", response.text)
except Exception as e:
    print("오류 발생:", str(e))