import httpx
import os

class TeraflopAI:
    def __init__(self, api_key: str, url: str):
        self.url = url
        self.api_key = api_key or os.getenv("TERAFLOPAI_API_KEY")
        self.client = httpx.Client(
            http2 = True,
            timeout = 30.0,
            headers = {"Authorization": f"Bearer {self.api_key}"}
        )

    def search(self, query: str):
        return self.post(query)
    
    def segment(self, query: str):
        return self.post(query)
    
    def post(self, query: str):
        payload = {"query": f"{query}"}
        result = self.client.post(self.url, json=payload)
        result.raise_for_status()
        return result.json()