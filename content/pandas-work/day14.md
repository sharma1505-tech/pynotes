---
title: Day14
date: 2026-04-21
author: Your Name
cell_count: 4
score: 0
---

```python
student = {}

name = input("Enter name: ")
marks = int(input("Enter marks: "))

student["name"] = name
student["marks"] = marks

print("Student Details:", student)
```

    Enter name:  Sri
    Enter marks:  95
    

    Student Details: {'name': 'Sri', 'marks': 95}
    


```python
text = input("Enter sentence: ")
words = text.split()

count = {}

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

print("Word Count:", count)
```

    Enter sentence:  Sridharshini
    

    Word Count: {'Sridharshini': 1}
    


```python
data = {"a": 10, "b": 20, "c": 30}

key = input("Enter key to search: ")

if key in data:
    print("Value:", data[key])
else:
    print("Key not found")
```

    Enter key to search:  b
    

    Value: 20
    


```python

```


---
**Score: 0**