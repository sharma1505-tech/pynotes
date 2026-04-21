---
title: Day29
date: 2026-04-21
author: Your Name
cell_count: 5
score: 5
---

```python
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["genai_db"]
collection = db["data"]
```


```python
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["genai_db"]
col = db["prompts"]

text = input("Enter prompt: ")

col.insert_one({"prompt": text})
print("Saved to DB")
```

    Enter prompt:  What is AI
    

    Saved to DB
    


```python
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["genai_db"]
col = db["prompts"]

for data in col.find():
    print(data)
```

    {'_id': ObjectId('69e6f95f646739d1bd2840cf'), 'prompt': 'What is AI'}
    


```python
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["genai_db"]
col = db["prompts"]

text = input("Enter prompt to delete: ")

col.delete_one({"prompt": text})
print("Deleted")
```

    Enter prompt to delete:  What is AI
    

    Deleted
    


```python

```


---
**Score: 5**