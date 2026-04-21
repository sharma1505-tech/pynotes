---
title: Day21
date: 2026-04-21
author: Your Name
cell_count: 4
score: 0
---

```python
import random

secret = random.randint(1, 50)
guess = 0

while guess != secret:
    guess = int(input("Guess number (1-50): "))
    
    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
    else:
        print("Correct! 🎉")
```

    Guess number (1-50):  40
    

    Too high
    

    Guess number (1-50):  20
    

    Too high
    

    Guess number (1-50):  1
    

    Too low
    

    Guess number (1-50):  15
    

    Too high
    

    Guess number (1-50):  10
    

    Too low
    

    Guess number (1-50):  12
    

    Correct! 🎉
    


```python
import random
import string

length = int(input("Enter password length: "))

chars = string.ascii_letters + string.digits + string.punctuation
password = ""

for i in range(length):
    password += random.choice(chars)

print("Generated Password:", password)
```

    Enter password length:  4
    

    Generated Password: m%b>
    


```python
import random

otp = random.randint(1000, 9999)
attempts = 3

print("OTP sent:", otp)  # real app la print panna koodathu

while attempts > 0:
    user = int(input("Enter OTP: "))
    
    if user == otp:
        print("Verified ✅")
        break
    else:
        attempts -= 1
        print("Wrong OTP, attempts left:", attempts)

if attempts == 0:
    print("Blocked ❌")
```

    OTP sent: 4387
    

    Enter OTP:  5423
    

    Wrong OTP, attempts left: 2
    

    Enter OTP:  5415
    

    Wrong OTP, attempts left: 1
    

    Enter OTP:  8521
    

    Wrong OTP, attempts left: 0
    Blocked ❌
    


```python

```


---
**Score: 0**