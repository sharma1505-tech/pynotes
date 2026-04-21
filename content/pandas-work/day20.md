---
title: Day20
date: 2026-04-21
author: Your Name
cell_count: 5
score: 5
---

```python
import math

num = float(input("Enter number: "))

print("Square root:", math.sqrt(num))
print("Power (num^2):", math.pow(num, 2))
print("Ceil:", math.ceil(num))
print("Floor:", math.floor(num))
```

    Enter number:  50
    

    Square root: 7.0710678118654755
    Power (num^2): 2500.0
    Ceil: 50
    Floor: 50
    


```python
import random

otp = random.randint(1000, 9999)

print("Your OTP is:", otp)
```

    Your OTP is: 2586
    


```python
import mymodule

print("Addition:", mymodule.add(10, 5))
print("Subtraction:", mymodule.sub(10, 5))
def add(a, b):
    return a + b

def sub(a, b):
    return a - b
```


    ---------------------------------------------------------------------------

    ModuleNotFoundError                       Traceback (most recent call last)

    Cell In[7], line 1
    ----> 1 import mymodule
          3 print("Addition:", mymodule.add(10, 5))
          4 print("Subtraction:", mymodule.sub(10, 5))
    

    ModuleNotFoundError: No module named 'mymodule'



```python

```


    ---------------------------------------------------------------------------

    ModuleNotFoundError                       Traceback (most recent call last)

    Cell In[6], line 1
    ----> 1 import mymodule
          3 print("Addition:", mymodule.add(10, 5))
          4 print("Subtraction:", mymodule.sub(10, 5))
    

    ModuleNotFoundError: No module named 'mymodule'



```python

```


---
**Score: 5**