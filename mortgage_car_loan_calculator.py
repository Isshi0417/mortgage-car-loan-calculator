import json

with open('messages.json', 'r') as file:
    MESSAGES = json.load(file)

def prompt(key):
    message = MESSAGES[key]
    print(f"=> {message}")

# Welcome message
prompt("welcome")
# Explain what the program does
prompt("explanation")
# Ask for the total loan amount
prompt("ask_loan")
total_loan = float(input())
# Ask for the monthly interest rate
prompt("ask_interest")
monthly_interest = float(input())
# Ask for the duration of the loan (in months)
prompt("ask_duration")
duration = int(input())
# Do the math
monthly_payment = total_loan * (monthly_interest / 
                                (1 - (1 + monthly_interest) ** (-duration)))
# Print monthly payment
prompt("result")
print(f"=> {monthly_payment}")