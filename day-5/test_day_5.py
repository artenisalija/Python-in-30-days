from day_5 import process_task

def test_valid_task():
    task = {"id": 1, "name": "Backup"}
    result = process_task(task)
    assert "valid" in result.lower()


def test_missing_id():
    task = {"name": "Backup"}
    result = process_task(task)
    assert "no id" in result.lower()


def test_missing_name():
    task = {"id": 1}
    result = process_task(task)
    assert "no name" in result.lower()
