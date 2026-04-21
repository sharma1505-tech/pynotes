---
title: Day11
date: 2026-04-21
author: Your Name
cell_count: 4
score: 0
---

```python
def calculator(a, b):
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    
    if b != 0:
        print("Division:", a / b)
    else:
        print("Division not possible")

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

calculator(x, y)
```

    Enter first number:  10
    Enter second number:  5
    

    Addition: 15
    Subtraction: 5
    Multiplication: 50
    Division: 2.0
    


```python
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

num = int(input("Enter number: "))
print("Factorial:", factorial(num))
```

    Enter number:  5
    

    Factorial: 120
    


```python
def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

num = int(input("Enter number: "))

if is_prime(num):
    print("Prime Number")
else:
    print("Not Prime")
```

    Enter number:  5
    

    Prime Number
    


```python

```


---
**Score: 0**