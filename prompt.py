import streamlit as st
import time
import itertools
from groq import Groq

# ---------- SETUP ----------
# Set up API key securely
api_key = st.secrets["GROQ_API_KEY"]

# Set up avatars
logo_url = "https://raw.githubusercontent.com/CIBIRAJGL/WISP/main/Resources/Logo.png"
user_url = "https://raw.githubusercontent.com/CIBIRAJGL/WISP/main/Resources/User.png"
avatars = {"assistant": logo_url, "user": user_url}

# Page config
st.set_page_config(page_title='Wisp!', page_icon=logo_url)

# ---------- INIT ----------
if 'messages' not in st.session_state:
    st.session_state.messages = []

# ---------- HEADER ----------
st.markdown("# Hey Wisp! 🤖")
with st.chat_message(name="assistant", avatar=logo_url):
    st.markdown("### Ask your Queries!")

# ---------- FUNCTION ----------
def AI_(inp):
    try:
        client = Groq(api_key=api_key)
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": inp}],
            model="llama3-70b-8192",
            stream=False,
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"[Error] {str(e)}"

# ---------- SHOW PREVIOUS MESSAGES ----------
for message in st.session_state.messages:
    role = message.get("role", "assistant")
    content = message.get("content", "")
    avatar = avatars.get(role, logo_url)
    with st.chat_message(name=role, avatar=avatar):
        st.markdown(content)

# ---------- USER INPUT ----------
if prompt := st.chat_input("Type here..."):
    # Show user input
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message(name="user", avatar=user_url):
        st.markdown(prompt)

    # Process and show response
    with st.chat_message(name="assistant", avatar=logo_url):
        message_placeholder = st.empty()
        full_response = ""

        with st.spinner("Thinking... 💭"):
            response = AI_(prompt)
            for chunk in response.split():
                full_response += chunk + " "
                time.sleep(0.05)
                message_placeholder.markdown(full_response + next(itertools.cycle(['', '.', '..', '...'])), unsafe_allow_html=True)
            message_placeholder.markdown(full_response)

    st.session_state.messages.append({"role": "assistant", "content": full_response})
