import streamlit as st
import google.generativeai as genai

# Page Config
st.set_page_config(page_title="Sukoon AI", page_icon="🌙")
st.title("🌙 Sukoon AI")

# API Key Connection (Secrets se)
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    # Sabse stable model name use kar rahe hain
    model = genai.GenerativeModel('gemini-pro')
    
except Exception as e:
    st.error(f"Setup Error: {e}")

# Chat History Setup
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Aaj aap kaisa feel kar rahe hain?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        try:
            # Empathy Logic
            system_instruction = "Tum Sukoon AI ho. Ek dost ki tarah Hinglish mein baat karo aur user ka dard samjho."
            response = model.generate_content(f"{system_instruction}\n\nUser: {prompt}")
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"AI Error: {e}")
            
