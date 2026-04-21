---
title: Day6
date: 2026-04-21
author: Your Name
cell_count: 4
score: 0
---

```python
num = int(input("Enter number: "))
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print("Reversed number:", rev)
```

    Enter number:  123
    

    Reversed number: 321
    


```python
num = int(input("Enter number: "))
count = 0

while num > 0:
    count += 1
    num = num // 10

print("Total digits:", count)
```

    Enter number:  123456
    

    Total digits: 6
    


```python
num = int(input("Enter number: "))
temp = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
```

    Enter number:  121
    

    Palindrome
    


```python

```


---
**Score: 0**