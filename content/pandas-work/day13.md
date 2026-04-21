---
title: Day13
date: 2026-04-21
author: Your Name
cell_count: 4
score: 0
---

```python
def fibonacci(n):
    series = []
    a, b = 0, 1
    
    for i in range(n):
        series.append(a)
        a, b = b, a + b
    
    return series

num = int(input("Enter terms: "))
print("Fibonacci Series:", fibonacci(num))
```

    Enter terms:  52
    

    Fibonacci Series: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903, 2971215073, 4807526976, 7778742049, 12586269025, 20365011074]
    


```python
def is_armstrong(n):
    power = len(str(n))
    total = 0
    temp = n
    
    while temp > 0:
        digit = temp % 10
        total += digit ** power
        temp //= 10
    
    return total == n

start = int(input("Enter start: "))
end = int(input("Enter end: "))

print("Armstrong numbers:")
for num in range(start, end + 1):
    if is_armstrong(num):
        print(num)
```

    Enter start:  1
    Enter end:  200
    

    Armstrong numbers:
    1
    2
    3
    4
    5
    6
    7
    8
    9
    153
    


```python
def is_perfect(n):
    total = 0
    
    for i in range(1, n):
        if n % i == 0:
            total += i
    
    return total == n

start = int(input("Enter start: "))
end = int(input("Enter end: "))

print("Perfect numbers:")
for num in range(start, end + 1):
    if is_perfect(num):
        print(num)
```

    Enter start:  1
    Enter end:  25
    

    Perfect numbers:
    6
    


```python

```


---
**Score: 0**