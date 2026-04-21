---
title: Day22
date: 2026-04-21
author: Your Name
cell_count: 4
score: 0
---

```python
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if sorted(str1) == sorted(str2):
    print("Anagram")
else:
    print("Not Anagram")
```

    Enter first string:  Sharma
    Enter second string:  Sridharsini
    

    Not Anagram
    


```python
nums = list(map(int, input("Enter numbers: ").split()))

n = len(nums) + 1
total = n * (n + 1) // 2

print("Missing number:", total - sum(nums))
```

    Enter numbers:  40
    

    Missing number: -37
    


```python
nums = list(map(int, input("Enter numbers: ").split()))

nums = list(set(nums))  # remove duplicates
nums.sort()

print("Second largest:", nums[-2])
```

    Enter numbers:  1 2 3 
    

    Second largest: 2
    


```python

```


---
**Score: 0**