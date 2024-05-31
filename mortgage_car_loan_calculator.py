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
        
    total_loan = float(total_loan)

    print("\n")
    prompt("ask_interest")
    monthly_interest = input()

    while invalid_number(monthly_interest):
        prompt("invalid_interest")
        monthly_interest = input()

    monthly_interest = float(monthly_interest)

    if (monthly_interest >= 1):
        monthly_interest /= 100

    print("\n")
    prompt("ask_duration")
    duration = input()

    while invalid_number(duration):
        prompt("invalid_duration")
        duration = input()

    duration = float(duration) 

    monthly_payment = total_loan * monthly_interest / \
                        (1 - (1 + monthly_interest) ** (-duration))
    
    print("\n")
    prompt("result", " ")
    print(monthly_payment)

    print("\n")
    prompt("another_one")
    answer = input().lower()
    if (answer and answer[0] != "y") or answer == "":
        break
    else:
        print("\n")