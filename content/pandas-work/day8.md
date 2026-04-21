---
title: Day8
date: 2026-04-21
author: Your Name
cell_count: 4
score: 0
---

```python
n = int(input("Enter number of elements: "))
nums = []

for i in range(n):
    val = int(input("Enter number: "))
    nums.append(val)

print("List:", nums)
```

    Enter number of elements:  2
    Enter number:  15
    Enter number:  25
    

    List: [15, 25]
    


```python
nums = [10, 45, 23, 89, 12]

max_val = nums[0]

for num in nums:
    if num > max_val:
        max_val = num

print("Maximum:", max_val)
```

    Maximum: 89
    


```python
nums = [10, 15, 22, 33, 40]

even = 0
odd = 0

for num in nums:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even count:", even)
print("Odd count:", odd)
```

    Even count: 3
    Odd count: 2
    


```python

```


---
**Score: 0**