import streamlit as st
import google.generativeai as genai

# Page setup
st.set_page_config(page_title="Sukoon AI", page_icon="🌙")
st.title("🌙 Sukoon AI")

# API Key connection
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# Chat History setup
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
        # Personality logic
        system_instruction = "Tum Sukoon AI ho. Tum ek empathetic therapist aur dost ho jo breakup ke dard ko samajhta hai. Hinglish mein baat karo."
        full_interaction = f"{system_instruction}\n\nUser: {prompt}"
        response = model.generate_content(full_interaction)
        st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
      
