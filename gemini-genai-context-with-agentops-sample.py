import google.generativeai as genai
import agentops
from agentops.agent import track_agent

GOOGLE_API_KEY=''
genai.configure(api_key=GOOGLE_API_KEY)
agentops.init('')

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
agentops.end_session('Success')