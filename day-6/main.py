from core.logic import process_request
from utils.helpers import format_result, error_message

def main():
    user_input = input("Enter a number: ")

    try:
        number = int(user_input)
    except EOFError:
        print("No input provided. Using default value 0.")
        user_input = "0"  # Or handle however you want

    result = process_request(number)

    if result is None:
        print(error_message())
    else:
        print(format_result(result))


if __name__ == "__main__":
    main()
