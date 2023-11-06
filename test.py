# Define two numbers
num1 = 10
num2 = 2

# Multiply the two numbers
result_multiply = num1 * num2
print(f"{num1} * {num2} = {result_multiply}")

# Divide the first number by the second number (check for division by zero)
if num2 != 0:
    result_divide = num1 / num2
    print(f"{num1} / {num2} = {result_divide}")
else:
    print("Division by zero is not allowed.")
