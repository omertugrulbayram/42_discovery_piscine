### 🔁 Exercise 3.0 – Up to 25

**Goal:**  
Use a `while` loop to display numbers from a user-given value up to 25.

---

**File:**  
- `to25.py`

---

**Implementation:**
```python
#!/usr/bin/env python3

num = int(input("Enter a number less than 25\n"))

if num > 25:
    print("Error")
else:
    while num <= 25:
        print(f"Inside the loop, my variable is {num}")
        num += 1
