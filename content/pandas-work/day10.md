---
title: Day10
date: 2026-04-21
author: Your Name
cell_count: 4
score: 0
---

```python
text = input("Enter text: ").lower()

vowels = "aeiou"
v_count = 0
c_count = 0

for ch in text:
    if ch.isalpha():
        if ch in vowels:
            v_count += 1
        else:
            c_count += 1

print("Vowels:", v_count)
print("Consonants:", c_count)
```

    Enter text:  a
    

    Vowels: 1
    Consonants: 0
    


```python
text = input("Enter text: ")

rev = ""
for ch in text:
    rev = ch + rev

print("Reversed:", rev)
```

    Enter text:  Shatrma
    

    Reversed: amrtahS
    


```python
text = input("Enter text: ")

rev = text[::-1]

if text == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
```

    Enter text:  madam
    

    Palindrome
    


```python

```


---
**Score: 0**