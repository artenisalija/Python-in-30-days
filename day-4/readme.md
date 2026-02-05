Day 4 – Pure Functions & Side Effects

Overview
Today I learned how professional software separates **logic** from **actions** using two types of functions:

- **Pure functions** – make decisions and return results  
- **Side-effect functions** – interact with the outside world (logging, printing, saving, etc)

This separation makes code predictable, testable, and safe to run in CI/CD pipelines.

---

What I Built
A small **gym membership system simulation**:

1. Validates whether a user is allowed to join  
2. Logs the result

This mirrors how real backend systems operate.

---

How the System Works
- Pure Validation Function
Checks business rules:

```python
def is_age_valid(age):
    return age >= 18
