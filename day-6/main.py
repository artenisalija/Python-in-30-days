from core.logic import process_request
from utils.helpers import format_result, error_message

def main():
    user_input = input("Enter a number: ")

    try:
        number = int(user_input)
    except ValueError:
        print(error_message())
        return

    result = process_request(number)

    if result is None:
        print(error_message())
    else:
        print(format_result(result))


if __name__ == "__main__":
    main()
