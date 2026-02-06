import streamlit as st
import google.generativeai as genai

# Configure Gemini using Streamlit secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

def generate_explanation(question, code="", mode="simple", history=None):
    if history is None:
        history = []
    
    system_prompt = (
        "Explain the code simply."
        if mode == "simple"
        else "Explain the code in detail with examples."
    )
    
    model = genai.GenerativeModel("gemini-2.5-flash")
    
    prompt = f"""
{system_prompt}

Question: {question}

Code:
{code}
"""
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Gemini error: {str(e)}"
