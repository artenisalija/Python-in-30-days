def individual_serial(todo) -> dict:
    return {
        "id": str(todo["_id"]),
        "title": todo.get("title"),  # <-- match what was actually inserted
        "description": todo.get("description"),
        "completed": todo.get("completed")  # <-- match actual field
    }


def list_serial(todos) -> list:
    return [individual_serial(todo) for todo in todos]


