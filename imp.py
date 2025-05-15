import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env
load_dotenv()

def AI_(inp):
    try:
        client = Groq(api_key="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")

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": inp,
                }
            ],
            model="llama3-70b-8192",  # Update if you use a different one
            stream=False,
        )

        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"[Error] {str(e)}"

if __name__ == "__main__":
    print("Type 'exit' to quit.")
    while True:
        inp = input("Enter: ")
        if inp.lower() in {"exit", "quit"}:
            break
        res = AI_(inp)
        print(res)
