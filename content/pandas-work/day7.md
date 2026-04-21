---
title: Day7
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

    Enter number of elements:  10
    Enter number:  10
    Enter number:  5
    Enter number:  2
    Enter number:  2
    Enter number:  2
    Enter number:  2
    Enter number:  2
    Enter number:  2
    Enter number:  2
    Enter number:  2
    

    List: [10, 5, 2, 2, 2, 2, 2, 2, 2, 2]
    


```python
n = int(input("Enter rows: "))

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
```

    Enter rows:  5
    

    * * * * * 
    * * * * 
    * * * 
    * * 
    * 
    


```python
n = int(input("Enter rows: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
```

    Enter rows:  2
    

    1 
    1 2 
    


```python

```


---
**Score: 0**