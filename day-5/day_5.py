# Custom error
class InvalidTaskError(Exception):
    pass


# 1) Validation (pure function)
def validate_task(task):
    if "id" not in task:
        raise InvalidTaskError("Task has no ID")

    if "name" not in task:
        raise InvalidTaskError("Task has no name")

    return True


# 2) Logging (side effect)
def log_error(message):
    print("LOG:", message)   # for beginners, we just print


# 3) Main logic
def process_task(task):
    try:
        validate_task(task)
        return "✅ Task is valid and processed"

    except InvalidTaskError as e:
        log_error(str(e))
        return "❌ " + str(e)
    

# Example usage
# --- Run the program ---
if __name__ == "__main__":
    print(process_task({"id": 1, "name": "Backup"}))
    print(process_task({"name": "Backup"}))
    print(process_task({"id": 2}))

