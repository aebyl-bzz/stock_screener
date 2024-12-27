from googlesearch import search

query = "Nestle"
for result in search(query, num_results=5):
    print(result)