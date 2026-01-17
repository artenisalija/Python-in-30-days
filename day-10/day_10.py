# day_10.py
"""
Entry point for Day 10 - 1-week keto diet suggestion.
"""

from diet import weekly_plan

def main():
    plan = weekly_plan()
    print("Your 7-day keto diet plan:\n")
    for day, meals in plan.items():
        print(day)
        for meal_name, meal in meals.items():
            print(f"  {meal_name}: {meal}")
        print()  # empty line between days

if __name__ == "__main__":
    main()
