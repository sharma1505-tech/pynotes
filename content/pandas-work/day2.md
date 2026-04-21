---
title: Day2
date: 2026-04-21
author: Your Name
cell_count: 4
score: 0
---

```python
a = int(input("Enter a: "))
b = int(input("Enter b: "))

a, b = b, a

print("After swap:")
print("a =", a)
print("b =", b)
```

    Enter a:  20
    Enter b:  10
    

    After swap:
    a = 10
    b = 20
    


```python
print("1.Circle  2.Rectangle")
choice = int(input("Enter choice: "))

if choice == 1:
    r = float(input("Enter radius: "))
    area = 3.14 * r * r
    print("Area of circle:", area)

elif choice == 2:
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    area = l * w
    print("Area of rectangle:", area)

else:
    print("Invalid choice")
```

    1.Circle  2.Rectangle
    

    Enter choice:  2
    Enter length:  10
    Enter width:  20
    

    Area of rectangle: 200.0
    


```python
p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

si = (p * r * t) / 100

print("Simple Interest:", si)
print("Total Amount:", p + si)
```

    Enter principal:  50
    Enter rate:  20
    Enter time:  2
    

    Simple Interest: 20.0
    Total Amount: 70.0
    


```python

```


---
**Score: 0**