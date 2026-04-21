---
title: Day24
date: 2026-04-21
author: Your Name
cell_count: 4
score: 0
---

```python
nums = list(map(int, input("Enter numbers: ").split()))
key = int(input("Enter element to search: "))

found = False

for i in range(len(nums)):
    if nums[i] == key:
        print("Found at index:", i)
        found = True
        break

if not found:
    print("Not found")
```

    Enter numbers:  55
    Enter element to search:  5
    

    Not found
    


```python
nums = sorted(list(map(int, input("Enter sorted numbers: ").split())))
key = int(input("Enter element to search: "))

low = 0
high = len(nums) - 1

while low <= high:
    mid = (low + high) // 2
    
    if nums[mid] == key:
        print("Found at index:", mid)
        break
    elif nums[mid] < key:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Not found")
```

    Enter sorted numbers:  55
    Enter element to search:  55
    

    Found at index: 0
    


```python
nums = list(map(int, input("Enter numbers: ").split()))
key = int(input("Enter element: "))

count = 0

for num in nums:
    if num == key:
        count += 1

print("Occurrences:", count)
```

    Enter numbers:  55
    Enter element:  55
    

    Occurrences: 1
    


```python

```


---
**Score: 0**