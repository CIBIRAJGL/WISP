import streamlit as st
import os
import time
import itertools
from groq import Groq

# Set Streamlit page configuration
logo_url = "https://raw.githubusercontent.com/CIBIRAJGL/WISP/main/Resources/Logo.png"
user_url = "https://raw.githubusercontent.com/CIBIRAJGL/WISP/main/Resources/User.png"
st.set_page_config(page_title='Wisp!', page_icon=logo_url)

# Define the AI function using Groq API
def AI_(inp):
    try:
        client = Groq(api_key=st.secrets["GROQ_API_KEY"])  # Use Streamlit secrets
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": inp,
                }
            ],
            model="llama3-70b-8192",
            stream=False,
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"[Error] {str(e)}"

# Store chat messages in session state
if 'messages' not in st.session_state:
    st.session_state.messages = []

avatars = {"assistant": logo_url, "user": user_url}

# Header
st.markdown("# Hey Wisp! 🤖")
with st.chat_message(name="assistant", avatar=avatars["assistant"]):
    st.markdown('### Ask your Queries!')

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(name=message["role"], avatar=avatars[message["role"]]):
        st.markdown(message["content"])

# Input and response
if prompt := st.chat_input("Type here.."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message(name="user", avatar=avatars["user"]):
        st.markdown(prompt)

    with st.chat_message(name="assistant", avatar=avatars["assistant"]):
        message_placeholder = st.empty()
        full_response = ""

        with st.spinner(text="Thinking... 💭💭💭"):
            raw = AI_(prompt)
            response = str(raw)

            # Typing effect
            dots = itertools.cycle(['', '.', '..', '...'])
            for chunk in response.split():
                full_response += chunk + " "
                time.sleep(0.05)
                message_placeholder.markdown(full_response + next(dots), unsafe_allow_html=True)

            message_placeholder.markdown(full_response)

        st.session_state.messages.append({"role": "assistant", "content": full_response})
