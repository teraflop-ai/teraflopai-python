from teraflopai import TeraflopAI

url = "https://api.teraflopai.com/v1/embeddings/free"

client = TeraflopAI(url=url)

results = client.embeddings(
    query=["City of Houma", "Text two"], 
    model="concept-embedding-legal-nano"
)

print(results)

results = client.embeddings(
    query="City of Houma", 
    model="concept-embedding-legal-nano"
)

print(results)