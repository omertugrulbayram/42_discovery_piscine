### ➖➕ Exercise 2.1 – Am I Negative?

**Goal:**  
Use conditional statements to determine whether a number is negative, positive, or zero.

---

**File:**  
- `isneg.py`

---

**Implementation:**
```python
#!/usr/bin/env python3

number = int(input())

if number < 0:
    print("This number is negative.")
elif number > 0:
    print("This number is positive.")
else:
    print("This number is both positive and negative.")
