### 🔐 Exercise 2.2 – Passwords

**Goal:**  
Use conditional statements to validate a password entered by the user.

---

**File:**  
- `password.py`

---

**Implementation:**
```python
#!/usr/bin/env python3

password = "Python is awesome"

user_input = input()

if user_input == password:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")
