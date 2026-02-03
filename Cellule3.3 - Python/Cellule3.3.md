### 🔁 Exercise 3.3 – advanced_mult

**Goal:**  
Use nested `while` loops to display all multiplication tables from 0 to 10.

---

**File:**  
- `advanced_mult.py`

---

**Implementation:**
```python
#!/usr/bin/env python3

i = 0
while i <= 10:
    print("Table de " + str(i) + ":", end=" ")
    j = 0
    while j <= 10:
        print(i * j, end=" ")
        j += 1
    print()
    i += 1
