# Mortgage / Car Loan Calculator

A simple mortgage / car loan calculator. It takes the total loan amount, monthly interest rate, and loan duration (in months) to calculate the monthly payment.

This program uses the standard formula to calculate the loans:
$$monthly\ payment = loan\ amount * ( \frac{monthly\ interest\ rate}{1 - (1 + monthly\ interest\ rate)^{-loan\ duration\ in\ months}} )$$

### Program Process

The program first asks whether your desired currency has a decimal place or not. Depending on the input, it asks how many decimal places your currency uses. 

It then asks for the `loan amount`, `monthly interest`, and `loan duration` in months respectively.

> [!NOTE]
>
> `loan amount`, `monthly interest`, and `loan duration` need to be a numerical value such as `int` or `float`. Any other data types will result in an error and ask for a re-input.

It prints the result (`monthly interest rate`) that fits the characteristics of your currency format.

