---
title: Day16
date: 2026-04-21
author: Your Name
cell_count: 4
score: 0
---

```python
file = open("data.txt", "w")

text = input("Enter text: ")
file.write(text)

file.close()

print("Data written to file")
```

    Enter text:  only one
    

    Data written to file
    


```python
file = open("data.txt", "r")

content = file.read()

print("File Content:")
print(content)

file.close()
```

    File Content:
    only one
    


```python
file = open("data.txt", "r")

content = file.read()
words = content.split()

print("Total words:", len(words))

file.close()
```

    Total words: 2
    


```python

```


---
**Score: 0**