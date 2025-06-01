num1 = float(input("Enter the first number:"))
num2 = float (input("Enter the second number:"))
operation = input("Choose the operation (+, -, *, /):").strip()
result = None
match operation:
    case "+":
        rusult = num1 + num2
    case "-":
        rusult = num1 - num2
    case "*":
        rusult = num1 * num2
    case "/":
        if num2 != 0:
                result = num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Invalid operator. Please choose from +, -, *, or /.")

print(f"The result is {result}")