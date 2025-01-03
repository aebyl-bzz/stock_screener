import openai
from googlesearch import search

query = "Nestle BBC"
results = [result for result in search(query, num_results=5)]  # Save results in a list

# Print the search results
for result in results:
    print(result)

openai.api_key = "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"
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