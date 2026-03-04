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

### Search Engine API
```python
import os
from teraflopai import TeraflopAI

api_key = os.environ.get("TERAFLOPAI_API_KEY")

url = "https://api.caselaw.teraflopai.com/v1/search/free"

client = TeraflopAI(api_key=api_key, url=url)

results = client.search("City of Houma")

print(results["results"])
```

### Segmentation API
```python
import os
from teraflopai import TeraflopAI

api_key = os.environ.get("TERAFLOPAI_API_KEY")

url = "https://api.segmentation.teraflopai.com/v1/segmentation/free"

client = TeraflopAI(api_key=api_key, url=url)

text = """
UNITED STATES of America, Appellee, v. Daniel Dee VEON, Appellant.
No. 72-1889.
United States Court of Appeals, Ninth Circuit.
Feb. 12, 1973.

Claude 0. Allen, Oakland, Cal., for appellant.
James L. Browning, Jr., U. S. Atty., F. Steele Langford and Jerry K. Cimmet, Asst. U. S. Attys., San Francisco, Cal., for appellee.
Before TRASK, GOODWIN and WALLACE, Circuit Judges.
PER CURIAM:

Daniel Dee Veon appeals from convictions of violations of 21 U.S.C. § 841 (a) (1) (possession of marijuana with intent to distribute); two counts of 21 U.S.C. § 843(b) (use of telephone to commit or to facilitate commission of felonies under Title 21); 21 U.S.C. § 846 (conspiracy to distribute and to possess with intent to distribute marijuana).

Defendant contends the district court erred: (1) in restricting the reeross-examination of a government witness; (2) in receiving into evidence a tape recording and a written transcript of the tape; and (3) in submitting the case to the jury, upon evidence which he asserts was insufficient to support the verdict.

Customs agents observed a load of 400 kilograms of marijuana being brought in from Mexico. The agents arrested the smugglers and had them make a “controlled delivery” to Donald Lynch, their employer. Lynch was arrested and agreed to cooperate with police. With police listening and taping the call, Lynch phoned Veon and told him that the “stuff” was in for “Gary.” Veon said, “Yeah, okay, uh?” Lynch replied, “Same old thing.” Veon signified assent. This call is the basis for the second count of the indictment.
"""

results = client.segment(text)

print(results["results"])
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