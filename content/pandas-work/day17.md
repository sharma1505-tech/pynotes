---
title: Day17
date: 2026-04-21
author: Your Name
cell_count: 4
score: 0
---

```python
try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    
    result = a / b
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

except ValueError:
    print("Error: Invalid input")
```

    Enter a:  50
    Enter b:  60
    

    Result: 0.8333333333333334
    


```python
try:
    nums = list(map(int, input("Enter numbers: ").split()))
    index = int(input("Enter index: "))
    
    print("Element:", nums[index])

except ValueError:
    print("Invalid number input")

except IndexError:
    print("Index out of range")
```

    Enter numbers:  5
    Enter index:  6
    

    Index out of range
    


```python
try:
    file = open("data.txt", "r")
    content = file.read()
    print(content)

except FileNotFoundError:
    print("File not found")

finally:
    print("Execution completed")
```

    only one
    Execution completed
    


```python

```


---
**Score: 0**