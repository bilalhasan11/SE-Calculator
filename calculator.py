def addition(x, y):
    return x + y
def subtraction(x, y):
    return x - y
def multiplication(x, y):
    return x * y
def division(x, y):
    if y == 0:
        return "Division by zero is not allowed"
    return x / y
while True:
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'quit' to exit the program")
    
    user_choice = input(": ")
    
    if user_choice == "quit":
        break
    elif user_choice in ("add", "subtract", "multiply", "divide"):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        if user_choice == "add":
            print("Result:", addition(num1, num2))
        elif user_choice == "subtract":
            print("Result:", subtraction(num1, num2))
        elif user_choice == "multiply":
            print("Result:", multiplication(num1, num2))
        elif user_choice == "divide":
            print("Result:", division(num1, num2))
    else:
        print("Invalid input. Please try again.")