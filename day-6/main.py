import sys
from core.logic import process_request
from utils.helpers import format_result, error_message


def main():
    # If a value was passed from the command line (CI, Docker, etc)
    if len(sys.argv) > 1:
        user_input = sys.argv[1]
    else:
        # Otherwise, allow interactive input (local use)
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
