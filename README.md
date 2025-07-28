# Teraflop AI Python API library

## Installation
```bash
# install from PyPI
pip install teraflopai
```

## Usage
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