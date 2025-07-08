# teraflop-python

```python
from teraflop import TeraflopAI
        
client = TeraflopAI()
    
response = client.embed(
    input=[
        "YOUR TEXT HERE",
        "YOUR TEXT HERE"
    ],
    model="teraflopai-embed-law-0.1"
)
    
print(response.data[0].embedding)
```