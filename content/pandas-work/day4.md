---
title: Day4
date: 2026-04-21
author: Your Name
cell_count: 4
score: 0
---

```python
username = input("Enter username: ")
password = input("Enter password: ")

if username == "sharma":
    if password == "1525":
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("Invalid Username")
```

    Enter username:  sharma
    Enter password:  1525
    

    Login Successful
    


```python
balance = 10000
amount = int(input("Enter amount to withdraw: "))

if amount <= balance:
    if amount % 100 == 0:
        print("Please collect cash")
        balance -= amount
        print("Remaining balance:", balance)
    else:
        print("Enter amount in multiples of 100")
else:
    print("Insufficient balance")
```

    Enter amount to withdraw:  10000
    

    Please collect cash
    Remaining balance: 0
    


```python
units = int(input("Enter units: "))

if units <= 100:
    bill = units * 2
elif units <= 200:
    bill = (100 * 2) + (units - 100) * 3
else:
    bill = (100 * 2) + (100 * 3) + (units - 200) * 5

print("Total bill:", bill)
```

    Enter units:  15
    

    Total bill: 30
    


```python

```


---
**Score: 0**