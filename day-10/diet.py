# diet.py
"""
This module provides keto diet suggestions for one week.
"""

from random import choice

# Simple keto meals
MEALS = {
    "breakfast": [
        "Scrambled eggs with avocado",
        "Bacon and spinach omelette",
        "Greek yogurt with seeds",
    ],
    "lunch": [
        "Grilled chicken salad with olive oil",
        "Tuna salad with avocado",
        "Beef stir-fry with broccoli",
    ],
    "dinner": [
        "Salmon with asparagus",
        "Grilled steak with spinach",
        "Zucchini noodles with pesto and chicken",
    ],
}

def suggest_meal(meal_type: str) -> str:
    """Return a random meal suggestion for the given type."""
    if meal_type not in MEALS:
        return "Meal type not found!"
    return choice(MEALS[meal_type])

def weekly_plan() -> dict:
    """Generate a simple 7-day keto plan."""
    plan = {}
    for day in range(1, 8):
        plan[f"Day {day}"] = {
            "Breakfast": suggest_meal("breakfast"),
            "Lunch": suggest_meal("lunch"),
            "Dinner": suggest_meal("dinner"),
        }
    return plan
