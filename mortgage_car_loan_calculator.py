import json

with open('messages.json', 'r') as file:
    MESSAGES = json.load(file)

def prompt(key):
    message = MESSAGES[key]
    print(f"=> {message}")

while True:
    prompt("welcome")
    prompt("explanation")
    prompt("ask_loan")
    prompt("ask_interest")
    monthly_interest = float(input())
    prompt("ask_duration")
    duration = int(input())
    monthly_payment = total_loan * (monthly_interest / 
                                    (1 - (1 + monthly_interest) ** (-duration)))
    prompt("result")
    print(f"=> {monthly_payment}")

    prompt("another_one")
    answer = input().lower()
    if (answer and answer[0] != "y") or answer == "":
        break