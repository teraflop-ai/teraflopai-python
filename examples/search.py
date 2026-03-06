from teraflopai import TeraflopAI

url = "https://api.caselaw.teraflopai.com/v1/search/free"

client = TeraflopAI(url=url)

results = client.search("City of Houma")

print(results["results"])