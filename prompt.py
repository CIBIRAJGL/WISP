import streamlit as st
import time
import itertools
import imp  # Keeping imp as per your request

# Use RAW GitHub URLs for images
logo_url = "https://raw.githubusercontent.com/CIBIRAJGL/WISP/main/Logo.png"
user_url = "https://raw.githubusercontent.com/CIBIRAJGL/WISP/main/user.png"

st.set_page_config(page_title='Wisp!', page_icon= logo_url)

# Store messages
if 'messages' not in st.session_state:
    st.session_state.messages = []


avatars = {"assistant": logo_url, "user": user_url}

st.markdown("# Hey Wisp! 🤖")

with st.chat_message(name="assistant", avatar=avatars["assistant"]):
    st.markdown('### Ask your Queries!')

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(name=message["role"], avatar=avatars[message["role"]]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Type here.."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message
    with st.chat_message(name="user", avatar=avatars["user"]):
        st.markdown(prompt)

    # Display assistant response
    with st.chat_message(name="assistant", avatar=avatars["assistant"]):
        message_placeholder = st.empty()
        full_response = ""

        with st.spinner(text="Thinking... 💭💭💭"):
            raw = imp.AI_(prompt)  # Keeping the original imp module usage
            response = str(raw)

            # Typing effect
            dots = itertools.cycle(['', '.', '..', '...'])
            for chunk in response.split():
                full_response += chunk + " "
                time.sleep(0.05)
                message_placeholder.markdown(full_response + next(dots), unsafe_allow_html=True)

            message_placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
