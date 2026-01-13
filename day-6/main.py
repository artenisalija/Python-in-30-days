from core.logic import process_request
from utils.helpers import format_result, error_message

def main():
    # Try reading input safely
    try:
        user_input = input("Enter a number: ")
    except EOFError:
        print("No input provided. Using default value 0.")
        user_input = "0"  # fallback for CI

    # Convert input to integer safely
    try:
        number = int(user_input)
    except ValueError:
        print(error_message())
        return
    except Exception:
        print("Unexpected error converting input.")
        return

    # Run core logic
    result = process_request(number)

    if result is None:
        print(error_message())
    else:
        print(format_result(result))


if __name__ == "__main__":
    main()
