from groq import Groq

def AI_(inp):
    client = Groq(
        api_key="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"
    )
    chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": inp,
                }
            ],
            model="llama-3.3-70b-versatile",
            stream=False,
    )

    return chat_completion.choices[0].message.content

if __name__=="__main__":
     while True:
        inp = input("enter:")
        res = AI_(inp)
        print(res)



