import httpx

class TeraflopAI:
    def __init__(self, api_key: str, url: str):
        self.url = url
        self.client = httpx.Client(
            http2 = True,
            timeout = 30.0,
            headers = {"Authorization": f"Bearer {api_key}"}
        )

    def search(self, query: str):
        payload = {"query": f"{query}"}
        result = self.client.post(self.url, json=payload)
        result.raise_for_status()
        return result.json()
    
    def segment(self, query: str):
        payload = {"query": f"{query}"}
        result = self.client.post(self.url, json=payload)
        result.raise_for_status()
        return result.json()