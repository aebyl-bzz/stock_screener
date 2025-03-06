import openai
from googlesearch import search

query = "Nestle BBC"
results = [result for result in search(query, num_results=5)]

for result in results:
    print(result)

openai.api_key = "apikey"
chat_completion = openai.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content":f"is there any bad news mentioned in the following links?{results}",
            "max_tokens":60

        }
    ],
    model="gpt-4",
)

print(chat_completion)