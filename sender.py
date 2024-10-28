from groq import Groq
def give_commands(a):

    client = Groq(
        api_key=r'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',
            )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": a,
            }
        ],
        model="llama3-8b-8192",
            )

    print(chat_completion.choices[0].message.content)