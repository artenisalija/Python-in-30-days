from db import get_connection

def create_table():
    conn = get_connection()
    cur = conn.cursor()
    with open("schema.sql") as f:
        cur.execute(f.read())
    conn.commit()
    cur.close()
    conn.close()

def add_food():
    name = input("Food name: ")
    calories = int(input("Calories: "))
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO foods (name, calories) VALUES (%s, %s)", (name, calories))
    conn.commit()
    cur.close()
    conn.close()
    print(f"{name} added!")

def list_foods():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, calories FROM foods")
    rows = cur.fetchall()
    for r in rows:
        print(f"{r[0]}: {r[1]} - {r[2]} kcal")
    cur.close()
    conn.close()

def main():
    create_table()
    while True:
        print("\n1. Add Food")
        print("2. List Foods")
        print("0. Exit")
        choice = input("Choose: ")
        if choice == "1":
            add_food()
        elif choice == "2":
            list_foods()
        elif choice == "0":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
