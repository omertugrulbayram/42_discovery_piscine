### 🔁 Exercise 3.2 – i_got_that

**Goal:**  
Use a `while` loop to continuously accept user input until a specific keyword is entered.

---

**File:**  
- `i_got_that.py`

---

**Implementation:**
```python
#!/usr/bin/env python3

while True:
    user_input = input("What you gotta say? : ")
    if user_input == "STOP":
        break
    print("I got that! Anything else? :", end=" ")
