import json

# Read JSON file
with open('messages.json', 'r') as file:
    MESSAGES = json.load(file)

# Methods
def prompt(key, format = "\n"):
    message = MESSAGES[key]
    print(f" -> {message}", end = format)

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True
    
    return False

# Calculator Program
while True:
    prompt("welcome")
    prompt("explanation")
    print("\n")

    prompt("ask_loan")
    total_loan = input()

    while invalid_number(total_loan):
        prompt("invalid_loan")
        total_loan = input()

    print("\n")
    prompt("ask_interest")
    monthly_interest = input()

    while invalid_number(monthly_interest):
        prompt("invalid_interest")
        monthly_interest = input()

    print("\n")
    prompt("ask_duration")
    duration = input()

    while invalid_number(duration):
        prompt("invalid_duration")
        duration = input()

    monthly_payment = float(total_loan) * (float(monthly_interest) / 
                    (1 - (1 + float(monthly_interest)) ** (-float(duration))))
    
    print("\n")
    prompt("result", " ")
    print(monthly_payment)

    print("\n")
    prompt("another_one")
    answer = input().lower()
    if (answer and answer[0] != "y") or answer == "":
        break