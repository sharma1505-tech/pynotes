---
title: Day19
date: 2026-04-21
author: Your Name
cell_count: 4
score: 0
---

```python
class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Name:", self.name)

class Student(Person):
    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks

    def display(self):
        self.show()
        print("Marks:", self.marks)

s = Student("Sharma", 85)
s.display()
```

    Name: Sharma
    Marks: 85
    


```python
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

d = Dog()
d.sound()
```

    Dog barks
    


```python
class Bird:
    def fly(self):
        print("Bird can fly")

class Penguin(Bird):
    def fly(self):
        print("Penguin cannot fly")

for obj in [Bird(), Penguin()]:
    obj.fly()
```

    Bird can fly
    Penguin cannot fly
    


```python

```


---
**Score: 0**