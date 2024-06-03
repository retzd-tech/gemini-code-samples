import google.generativeai as genai

GOOGLE_API_KEY='YOUR_API_KEY'
genai.configure(api_key=GOOGLE_API_KEY)

prompt = """
QUERY: who is the best employee in suroboyo restaurant in 2023 ?.
CONTEXT:

Best employee in suroboyo restaurant in 2023
Spongebob, January
Patrick, February
Plankton, March
Larry, April
Spongebob, May
Larry, June
Spongebob, July
Patrick, August
Spongebob, September
Spongebob, October
Plankton, November
Sandy, December
"""
model = genai.GenerativeModel(model_name='gemini-1.5-flash-latest')
print(model.generate_content(prompt).text)