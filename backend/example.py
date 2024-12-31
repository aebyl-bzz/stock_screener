import openai

openai.api_key = "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"
chat_completion = openai.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content":"Translate the following English text to French: 'Hello, how are you?'",
            "max_tokens":60

        }
    ],
    model="gpt-3.5-turbo",
)

print(chat_completion)