### 📊 Exercise 3.1 – Multiplication Table

**Goal:**  
Use loops to display the multiplication table of a given number.

---

**File:**  
- `multiplication_table.py`

---

**Implementation:**
```python
#!/usr/bin/env python3

num = int(input("Enter a number\n"))

i = 0
while i <= 9:
    print(f"{i} x {num} = {i * num}")
    i += 1
