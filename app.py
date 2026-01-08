import streamlit as st
import google.generativeai as genai

# Page Config
st.set_page_config(page_title="Sukoon AI", page_icon="🌙")
st.title("🌙 Sukoon AI")

# API Setup
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

# FINAL FIX FOR MODEL NAME
# Version v1beta ke liye sirf 'gemini-1.5-flash' kaafi hota hai
model = genai.GenerativeModel('gemini-1.5-flash')

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
if prompt := st.chat_input("Aaj aap kaisa feel kar rahe hain?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        try:
            # Sukoon Personality logic
            instruction = "Tum Sukoon AI ho. Hinglish mein baat karo aur user ke breakup ke dard ko samjho."
            response = model.generate_content(f"{instruction}\n\nUser: {prompt}")
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"AI Error: {e}")
            
            
