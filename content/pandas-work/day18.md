---
title: Day18
date: 2026-04-21
author: Your Name
cell_count: 4
score: 0
---

```python
class Student:
    def display(self):
        print("This is a student class")

s1 = Student()
s1.display()
```

    This is a student class
    


```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

s1 = Student("Sharma", 90)
s1.show()
```

    Name: Sharma
    Marks: 90
    


```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def grade(self):
        if self.marks >= 90:
            print(self.name, "- Grade A")
        elif self.marks >= 50:
            print(self.name, "- Pass")
        else:
            print(self.name, "- Fail")

name = input("Enter name: ")
marks = int(input("Enter marks: "))

s = Student(name, marks)
s.grade()
```

    Enter name:  Sridharshini
    Enter marks:  91
    

    Sridharshini - Grade A
    


```python

```


---
**Score: 0**