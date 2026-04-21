---
title: Day5
date: 2026-04-21
author: Your Name
cell_count: 4
score: 0
---

```python
num = int(input("Enter number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
```

    Enter number:  5
    

    5 x 1 = 5
    5 x 2 = 10
    5 x 3 = 15
    5 x 4 = 20
    5 x 5 = 25
    5 x 6 = 30
    5 x 7 = 35
    5 x 8 = 40
    5 x 9 = 45
    5 x 10 = 50
    


```python
n = int(input("Enter n: "))
total = 0

for i in range(1, n + 1):
    total += i

print("Sum =", total)
```

    Enter n:  5
    

    Sum = 15
    


```python
n = int(input("Enter rows: "))

for i in range(1, n + 1):
    for j in range(i):
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

```


---
**Score: 0**