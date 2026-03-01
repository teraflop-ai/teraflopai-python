# Teraflop AI Python API library

## Installation
```bash
# install from PyPI
pip install teraflopai
```

## Usage

```bash
export TERAFLOPAI_API_KEY="your_api_key_here"
```

Search Engine API
```python
import os
from teraflopai import TeraflopAI

api_key = os.environ.get("TERAFLOPAI_API_KEY")

url = "https://api.caselaw.teraflopai.com/v1/search/free"

client = TeraflopAI(api_key=api_key, url=url)

results = client.search("City of Houma")

print(results["results"][0])
```

### Beta functionality only available upon request

OpenAI compatible API 
```python
import os
from openai import OpenAI

client = OpenAI(
    base_url="",
    api_key=os.environ.get("TERAFLOPAI_API_KEY"),
)

response = client.embeddings.create(
    input=[
        "Your text string goes here",
        "Another text string",
    ],
    model=""
)

print(response)
```