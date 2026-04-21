---
title: Day9
date: 2026-04-21
author: Your Name
cell_count: 4
score: 0
---

```python
nums = list(map(int, input("Enter numbers: ").split()))
unique = []

for num in nums:
    if num not in unique:
        unique.append(num)

print("List without duplicates:", unique)
```

    Enter numbers:  5
    

    List without duplicates: [5]
    


```python
nums = list(map(int, input("Enter numbers: ").split()))

largest = second = -999999

for num in nums:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Second largest:", second)
```

    Enter numbers:  50
    

    Second largest: -999999
    


```python
list1 = list(map(int, input("Enter list1: ").split()))
list2 = list(map(int, input("Enter list2: ").split()))

merged = list1 + list2

print("Merged list:", merged)
```

    Enter list1:  1 2 3 5
    Enter list2:  1 2 4 8
    

    Merged list: [1, 2, 3, 5, 1, 2, 4, 8]
    


```python

```


---
**Score: 0**