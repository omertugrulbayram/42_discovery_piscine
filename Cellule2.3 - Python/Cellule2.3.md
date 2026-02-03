### ✖️ Exercise 2.3 – Multiplication

**Goal:**  
Use conditional statements to analyze the result of multiplying two numbers.

---

**File:**  
- `mult.py`

---

**Implementation:**
```python
#!/usr/bin/env python3

a = int(input("Enter the first number:\n"))
b = int(input("Enter the second number:\n"))

result = a * b

print(f"{a} x {b} = {result}")

if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")
