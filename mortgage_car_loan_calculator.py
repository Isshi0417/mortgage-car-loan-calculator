import json

with open('messages.json', 'r') as file:
    MESSAGES = json.load(file)

# Welcome message
print(MESSAGES["welcome"])
# Explain what the program does
print(MESSAGES["explanation"])
# Ask for the total loan amount
total_loan = float(input(MESSAGES["ask_loan"]))
# Ask for the monthly interest rate
monthly_interest = float(input(MESSAGES["ask_interest"]))
# Ask for the duration of the loan (in months)
duration = int(input(MESSAGES["ask_duration"]))
# Do the math
monthly_payment = total_loan * (monthly_interest / 
                                (1 - (1 + monthly_interest) ** (-duration)))
# Print monthly payment
print(MESSAGES["result"], monthly_payment)