---
title: Day30
date: 2026-04-21
author: Your Name
cell_count: 4
score: 0
---

```python
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Create / select database
db = client["mydatabase"]

# Create / select collection
col = db["mycollection"]

# User input
text = input("Enter topic: ")
result = "AI text about " + text

# Insert into MongoDB
col.insert_one({"topic": text, "result": result})

print(result)
```

    Enter topic:  What is AI
    

    AI text about What is AI
    


```python
for data in col.find():
    print(data)
```

    {'_id': ObjectId('69e6fe20f110c44a7a9671b9'), 'topic': 'What is AI', 'result': 'AI text about What is AI'}
    


```python
idea = input("Delete idea: ")
col.delete_one({"idea": idea})
print("Deleted")
```

    Delete idea:  What is AI
    

    Deleted
    


```python

```


---
**Score: 0**