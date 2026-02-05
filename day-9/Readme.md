Day 9 – Unit Testing with Docker & CI/CD

Overview
On this day, I created a simple Python function and wrote a test for it to verify whether the function **passes or fails** correctly.

---

🧪 Testing with Docker
Since `pytest` is not installed on my local system, I used **Docker** to handle testing.

Inside the Docker container:
- Installed pytest:
  ```bash
  pip install pytest


I created a GitHub Actions workflow that:

- Builds the Docker container

- Runs the container

- Executes the tests automatically

- Fails the pipeline if any test fails

- Passes the pipeline if all tests succeed