# ================================
# TASK MANAGER — OLD WAY vs NEW WAY
# ================================

import json
from dataclasses import dataclass, asdict


# ------------------------------------------------------------------
# ❌ OLD WAY — Manual class (commented out)
# ------------------------------------------------------------------

"""
class Task:
    def __init__(self, name, priority, done):
        self.name = name
        self.priority = priority
        self.done = done

    def __repr__(self):
        return f"Task(name={self.name}, priority={self.priority}, done={self.done})"

    def __eq__(self, other):
        return (
            self.name == other.name and
            self.priority == other.priority and
            self.done == other.done
        )


# Loading JSON the old way
with open("tasks.json", "r") as f:
    raw_tasks = json.load(f)

tasks = []
for task in raw_tasks:
    # You had to manually map dictionary keys
    t = Task(task["name"], task["priority"], task["done"])
    tasks.append(t)

# Saving back to JSON
data = []
for t in tasks:
    data.append({
        "name": t.name,
        "priority": t.priority,
        "done": t.done
    })

with open("tasks.json", "w") as f:
    json.dump(data, f, indent=2)
"""

# ------------------------------------------------------------------
# ✅ NEW WAY — Dataclasses + Type Hints
# ------------------------------------------------------------------

@dataclass
class Task:
    name: str
    priority: int
    done: bool


# Load JSON from file
with open("tasks.json", "r") as f:
    raw_tasks = json.load(f)

# Convert JSON dictionaries into Task objects
tasks = [Task(**task) for task in raw_tasks]

# Work with the tasks
for task in tasks:
    if not task.done:
        print(f"⏳ Pending: {task.name}")

# Mark "Cook pasta" as done
for task in tasks:
    if task.name == "Cook pasta":
        task.done = True

# Convert Task objects back to dictionaries
data = [asdict(task) for task in tasks]

# Save back to JSON
with open("tasks.json", "w") as f:
    json.dump(data, f, indent=2)

print("✅ Tasks updated and saved.")
