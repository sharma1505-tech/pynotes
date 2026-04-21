---
title: Day1
date: 2026-04-21
author: Your Name
cell_count: 4
score: 0
---

```python
name = input("Enter name: ")
marks = int(input("Enter marks: "))

print("\n--- Result ---")
print("Name:", name)

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Fail")
```

    Enter name:  sharma 
    Enter marks:  91
    

    
    --- Result ---
    Name: sharma 
    Grade: A
    


```python
print("1.Add  2.Sub  3.Mul  4.Div")
choice = int(input("Enter choice: "))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if choice == 1:
    print("Result:", a + b)
elif choice == 2:
    print("Result:", a - b)
elif choice == 3:
    print("Result:", a * b)
elif choice == 4:
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid choice")
```

    1.Add  2.Sub  3.Mul  4.Div
    

    Enter choice:  1
    Enter first number:  91
    Enter second number:  93
    

    Result: 184
    


```python
num = int(input("Enter number: "))

print("\n--- Analysis ---")

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

    Enter number:  66
    

    
    --- Analysis ---
    Positive
    Even
    


```python

```


---
**Score: 0**