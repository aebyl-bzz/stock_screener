import openai
from googlesearch import search

query = "Nestle BBC"
for result in search(query, num_results=5):
    print(result)

openai.api_key = "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"
chat_completion = openai.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content":f"is there any bad news mentioned in the following links?{result}",
            "max_tokens":60

        }
    ],
    model="gpt-4",
)

print(chat_completion)