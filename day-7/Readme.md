Day 7 – Python Tasks with Dataclasses & JSON

Overview
This project demonstrates how to **store, load, and manage tasks** in Python using **dataclasses** and **JSON**, following patterns commonly used in real-world applications.

---

🧠 What This Project Does
The script:
- Reads tasks from a JSON file
- Converts them into Python objects
- Updates task data
- Saves the updated tasks back to JSON

---

📦 Task Model
Tasks are represented using a Python dataclass:

```python
@dataclass
class Task:
    name: str
    priority: int
    done: bool

🛠 Technologies Used

- Python

- @dataclass

- Type hints

- JSON