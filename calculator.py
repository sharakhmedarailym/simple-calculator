def calculator():
    print("Simple Calculator")
    
    a = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    b = float(input("Enter second number: "))

    if operator == "+":
        result = a + b
    elif operator == "-":
        result = a - b
    elif operator == "*":
        result = a * b
    elif operator == "/":
        if b == 0:
            print("Error: division by zero")
            return
        result = a / b
    else:
        print("Unknown operator")
        return

    print("Result:", result)


if _name_ == "_main_":
    calculator()
