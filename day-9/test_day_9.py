# This file contains unit tests for day-9.py

from day_9 import add, divide


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    try:
        divide(10, 0)
        assert False  # should never reach this line
    except ZeroDivisionError:
        assert True
