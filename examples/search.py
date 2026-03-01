import os
from dotenv import load_dotenv
from teraflopai import TeraflopAI

load_dotenv()

api_key = os.environ.get("TERAFLOPAI_API_KEY")

url = "https://api.caselaw.teraflopai.com/v1/search/free"

client = TeraflopAI(api_key=api_key, url=url)

results = client.search("City of Houma")

print(results["results"][0])