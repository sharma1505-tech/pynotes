---
title: Day12
date: 2026-04-21
author: Your Name
cell_count: 4
score: 0
---

```python
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

num = int(input("Enter terms: "))
fibonacci(num)
```

    Enter terms:  2
    

    0 1 


```python
def is_armstrong(num):
    temp = num
    power = len(str(num))
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** power
        temp //= 10

    return total == num

n = int(input("Enter number: "))

if is_armstrong(n):
    print("Armstrong Number")
else:
    print("Not Armstrong")
```

    Enter number:  153
    

    Armstrong Number
    


```python
def is_perfect(n):
    total = 0
    
    for i in range(1, n):
        if n % i == 0:
            total += i

    return total == n

num = int(input("Enter number: "))

if is_perfect(num):
    print("Perfect Number")
else:
    print("Not Perfect")
```

    Enter number:  25
    

    Not Perfect
    


```python

```


---
**Score: 0**