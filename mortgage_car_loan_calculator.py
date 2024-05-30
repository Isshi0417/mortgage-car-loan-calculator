# Welcome message
print("Welcome to the Mortgage/Car Loan Calculator!")
# Explain what the program does
print("This program takes the total loan, monthly interest rate, and " 
      + "duration of the loan(in months) to calculate the monthly payment.")
# Ask for the total loan amount
total_loan = float(input("Please enter your total loan amount: "))
# Ask for the monthly interest rate
monthly_interest = float(input("Please enter your monthly interst rate: "))
# Ask for the duration of the loan (in months)
duration = int(input("Please enter the duration of the loan(in months): "))
# Do the math
monthly_payment = total_loan * (monthly_interest / 
                                (1 - (1 + monthly_interest) ** (-duration)))
# Print monthly payment
print("Your monthly payment is", monthly_payment)