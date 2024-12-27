import os
from openai import OpenAI

openai.api_key = "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" # This is the default and can be omitted

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
