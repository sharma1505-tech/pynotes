---
title: Day15
date: 2026-04-21
author: Your Name
cell_count: 5
score: 5
---

```python
t = (10, 20, 30, 40, 50)

print("Tuple:", t)
print("Length:", len(t))
print("First element:", t[0])
print("Last element:", t[-1])
```

    Tuple: (10, 20, 30, 40, 50)
    Length: 5
    First element: 10
    Last element: 50
    


```python
nums = list(map(int, input("Enter numbers: ").split()))

unique = set(nums)

print("Unique elements:", unique)
```

    Enter numbers:  50
    

    Unique elements: {50}
    


```python
set1 = set(map(int, input("Enter set1: ").split()))
set2 = set(map(int, input("Enter set2: ").split()))

common = set1.intersection(set2)

print("Common elements:", common)
```


```python
set1 = set(map(int, input("Enter set1: ").split()))
set2 = set(map(int, input("Enter set2: ").split()))

common = set1.intersection(set2)

print("Common elements:", common)

```

    Enter set1:  10 20 30 
    Enter set2:  50 40 30 
    

    Common elements: {30}
    


```python

```


---
**Score: 5**