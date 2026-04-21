---
title: Day3
date: 2026-04-21
author: Your Name
cell_count: 4
score: 0
---

```python
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a >= b and a >= c:
    print("A is largest:", a)
elif b >= a and b >= c:
    print("B is largest:", b)
else:
    print("C is largest:", c)
```

    Enter a:  10
    Enter b:  20
    Enter c:  15
    

    B is largest: 20
    


```python
marks = int(input("Enter marks: "))

if marks >= 50:
    print("Pass")
    
    if marks >= 90:
        print("Grade: A")
    elif marks >= 75:
        print("Grade: B")
    else:
        print("Grade: C")
else:
    print("Fail")
```

    Enter marks:  55
    

    Pass
    Grade: C
    


```python
age = int(input("Enter age: "))

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior Citizen")
```

    Enter age:  18
    

    Teenager
    


```python

```


---
**Score: 0**