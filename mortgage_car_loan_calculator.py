"""Import JSON module"""
import json

# Read JSON file
with open('messages.json', 'r', encoding="utf-8") as file:
    MESSAGES = json.load(file)

# Methods
def prompt(key, space = "\n"):
    """Prints messages in JSON file based on key"""
    message = MESSAGES[key]
    print(f" -> {message}", end = space)

def invalid_float(number_str):
    """Checks if param is a valid number"""
    try:
        float(number_str)
    except ValueError:
        return True

    return False

def invalid_int(number_str):
    """Checks if param is an integer"""
    try:
        int(number_str)
    except ValueError:
        return True

    return False

# Calculator Program

print(MESSAGES["divider"])
prompt("welcome")
prompt("explanation")
print(MESSAGES["divider"])

# Ask currency
prompt("ask_currency_format")
currency_format = input().lower()[0]

while currency_format not in ('y', 'n'):
    prompt("invalid_answer")
    currency_format = input().lower()

if currency_format == "y":
    print(MESSAGES["divider"])
    prompt("decimal_places")
    decimal_places = input()

    while invalid_int(decimal_places):
        prompt("invalid_integer")
        decimal_places = input()

    decimal_places = int(decimal_places)

print(MESSAGES["divider"])

# Calculations
while True:

    # Total loan
    prompt("ask_loan")
    total_loan = input()

    while invalid_float(total_loan):
        prompt("invalid_loan")
        total_loan = input()

    total_loan = float(total_loan)
    print(MESSAGES["divider"])

    # Monthly interest
    prompt("ask_interest")
    monthly_interest = input()

    while invalid_float(monthly_interest):
        prompt("invalid_interest")
        monthly_interest = input()

    monthly_interest = float(monthly_interest)

    if monthly_interest >= 1:
        monthly_interest /= 100

    print(MESSAGES["divider"])

    # Loan duration
    prompt("ask_duration")
    duration = input()

    while invalid_float(duration):
        prompt("invalid_duration")
        duration = input()

    duration = float(duration)

    # Monthly payment
    monthly_payment = total_loan * monthly_interest / \
                        (1 - (1 + monthly_interest) ** (-duration))

    print(MESSAGES["divider"])
    prompt("result", " ")

    if currency_format == "y":
        print(round(monthly_payment, decimal_places))
    else:
        print(round(monthly_payment))

    print(MESSAGES["divider"])

    # Repeated calculation
    prompt("another_one")
    answer = input().lower()

    if (answer and answer[0] != "y") or answer == "":
        break

    print(MESSAGES["divider"])
