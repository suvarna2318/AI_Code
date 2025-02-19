import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyB5ha47qhIXjI-0eNhUofY0-kr6c61JDnM")


sys_prompt = """You are an advanced Python code reviewer. Your task is to analyze the given Python code, 
identify potential bugs, logical errors, and areas of improvement, and suggest fixes.
Your response should be structured as follows:

1. *Issues Detected*: List any errors, inefficiencies, or improvements needed.
2. *Fixed Code*: Provide the corrected version of the code.
3. *Explanation*: Explain why the changes were made concisely.

If the code is already optimal, acknowledge it and suggest best practices."""


model = genai.GenerativeModel(model_name="gemini-1.5-flash", system_instruction=sys_prompt)


st.title("🔍 Python Code Reviewer with Gemini AI")
st.write("Paste your Python code below, and Gemini AI will analyze and suggest improvements.")


user_prompt = st.text_area("Enter your Python code:", height=200)

if st.button("Review Code"):
    if user_prompt.strip():
        # Generate AI response
        response = model.generate_content(user_prompt)
        st.subheader("📝 Review & Suggestions")
        st.markdown(response.text)  
    else:
        st.warning("⚠ Please enter some Python code before submitting.")
