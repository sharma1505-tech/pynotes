---
title: Day23
date: 2026-04-21
author: Your Name
cell_count: 4
score: 0
---

```python
n = int(input("Enter rows: "))

for i in range(1, n + 1):
    print(" " * (n - i), end="")
    
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
```

    Enter rows:  5
    

        * 
       * * 
      * * * 
     * * * * 
    * * * * * 
    


```python
n = int(input("Enter rows: "))
num = 1

for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
```

    Enter rows:  7
    

    1 
    2 3 
    4 5 6 
    7 8 9 10 
    11 12 13 14 15 
    16 17 18 19 20 21 
    22 23 24 25 26 27 28 
    


```python
n = int(input("Enter rows: "))

for i in range(n):
    num = 1
    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)
    print()
```

    Enter rows:  7
    

    1 
    1 1 
    1 2 1 
    1 3 3 1 
    1 4 6 4 1 
    1 5 10 10 5 1 
    1 6 15 20 15 6 1 
    


```python

```


---
**Score: 0**