### 🗣️ Exercise 1.3 – What’s your name?

**Goal:**  
Interact with the user by taking input and displaying a formatted message.

---

**File:**  
- `whatsyourname.py`

---

**Implementation:**
```python
first_name = input("Hey, what's your first name? : ").strip()
last_name = input("And your last name? : ").strip()

print(f"Well, pleased to meet you, {first_name} {last_name}.")
