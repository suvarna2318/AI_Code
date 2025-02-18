import streamlit as st
import google.generativeai as genai

# Set up Streamlit page configuration (optional)
st.set_page_config(
    page_title="Python Code Reviewer",
    page_icon=":computer:",
    layout="wide",  # Optional: Use a wider layout
)

# Streamlit App Title and Description
st.title("Python Code Reviewer")
st.markdown("Submit your Python code for automated review and receive a bug report with suggested fixes using Google's Gemini model.")

# Sidebar for API Key (Streamlit Secrets Management)
# This is the preferred approach for handling API keys
st.sidebar.header("API Configuration")
api_key = st.sidebar.text_input("Enter your Google API Key", type="password")
#This will use text input field to input api key

# Check if API key is provided
if not api_key:
    st.sidebar.warning("Please enter your Google API key to continue.")
    st.stop() # Stop the app if no key is provided

# Configure Generative AI model
try:
    genai.configure(api_key=api_key) # use a streamlit secret
    model = genai.GenerativeModel(model_name='gemini-pro',
                                system_instruction="""You are an advanced Python code reviewer. Your task is to analyze the given Python code, identify potential bugs, logical errors, and areas of improvement, and suggest fixes.
                Your response should be structured as follows:
                1. Issues Detected: List any errors, inefficiencies, or improvements needed.
                2. Fixed Code: Provide the corrected version of the code.
                3. Explanation: Explain why the changes were made concisely.

                If the code is already optimal, acknowledge it and suggest best practices."""
                                )
except Exception as e:
    st.error(f"Error configuring Gemini: {e}")
    st.stop()

# User Input - Code Editor
code = st.text_area("Enter your Python code:", height=300)

# Function to Generate Review Report
def generate_review(code):
    try:
        response = model.generate_content(code)
        return response.text
    except Exception as e:
        return f"Error generating review: {e}"

# Generate Report Button
if st.button("Generate Review"):
    if code:
        with st.spinner("Analyzing code with Gemini..."):
            report = generate_review(code)
            st.markdown("---")  # Add a horizontal line
            st.subheader("Review Report")
            st.write(report)
    else:
        st.warning("Please enter some Python code to analyze.")
