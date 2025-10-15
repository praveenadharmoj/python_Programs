num1 = float(input("Enter the first number :"))
operator = input("Enter an operator (+, -, *, /) :")
num2 = float(input("Enter the second number :"))

if operator == '+' :
    print(f"Sum of {num1} + {num2} is {num1 + num2} ")
elif operator == '-' :
    print(f"subtraction of {num1} - {num2} is {num1 - num2}")
elif operator == '*' :
    print(f"multiplication of {num1} * {num2} is {num1 * num2}")
elif operator == '/' :
    if num2 != 0 :
     print(f"Division of {num1} / {num2} is {num1 / num2}")
else :
    print("Error : Division by 0 is not allowed")