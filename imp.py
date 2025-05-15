import streamlit as st  # Required to access Streamlit's secrets
from groq import Groq  # Groq API client

# STEP 1: Function to get AI response from Groq

def ask_groq(prompt):
    """
    Takes a user prompt as input and returns the AI response using the Groq API.
    """
    try:
        # Get the API key from Streamlit secrets
        api_key = st.secrets["API_KEY"]

        # Initialize the Groq client
        client = Groq(api_key=api_key)

        # Send the user's message to the model
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="llama3-70b-8192",  # Make sure this matches your model from Groq
            stream=False,
        )

        # Return the model's response
        return chat_completion.choices[0].message.content

    except Exception as e:
        return f"[Error] {str(e)}"

# STEP 2: Main Streamlit interface

if __name__ == "__main__":
    import streamlit as st
    st.title("🧠 Wisp - Groq Chatbot")

    user_input = st.text_input("You:", placeholder="Ask me anything...")

    if user_input:
        if user_input.lower() in {"exit", "quit"}:
            st.write("👋 Exiting chatbot. Goodbye!")
        else:
            response = ask_groq(user_input)
            st.markdown(f"**Bot:** {response}")
