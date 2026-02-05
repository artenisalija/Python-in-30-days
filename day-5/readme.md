Day 5 – Error Handling, Logging & CI/CD

Overview
This project focuses on how real **backend** and **cloud systems** handle errors safely and reliably.

---

🧠 What I Learned

Custom Errors
A custom error (`InvalidTaskError`) is used to clearly signal invalid tasks instead of relying on generic Python exceptions.

Validation (Pure Function)
The validation logic only checks data and returns a result.  
It has no side effects, which makes it easy to test and reason about.

Logging (Side Effects)
When an error occurs, it is written to a log file (`errors.log`).  
This mirrors how production systems record failures.

Graceful Error Handling
Invalid input does not crash the program.  
Errors are caught, logged, and handled with a clean response.

CI/CD Pipeline
A GitHub Actions pipeline runs tests on every push.  
If error handling fails, the pipeline fails, preventing broken code from being merged.

---

💡 Why This Matters
This approach reflects how professional backend and cloud systems are built:
- Clear error definitions
- Safe error handling
- Automated testing
- Reliable deployments
