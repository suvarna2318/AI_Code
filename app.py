import google.generativeai as genai
from IPython.display import Markdown

genai.configure(api_key='AIzaSyB5ha47qhIXjI-0eNhUofY0-kr6c61JDnM')

sys_prompt="""You are an advanced Python code reviewer. Your task is to analyze the given Python code, identify potential bugs, logical errors, and areas of improvement, and suggest fixes.
                Your response should be structured as follows:
                1. Issues Detected: List any errors, inefficiencies, or improvements needed.
                2. Fixed Code: Provide the corrected version of the code.
                3. Explanation: Explain why the changes were made concisely.

                If the code is already optimal, acknowledge it and suggest best practices."""

model=genai.GenerativeModel(model_name='models/gemini-2.0-flash-exp',
                            system_instruction=sys_prompt)

user_prompt=input('Enter your Python code:')

response=model.generate_content(user_prompt)
print(response.text)
