num1 = float(input("Enter the first number1 : "))
num2 = float(input("Enter the second number2 : "))
operation= input("Choose the operation (+, -, *, /): ")

match operation :
    case "+":
        result = num1  + num2 
        print(f"The result of {num1} + {num2} is {result}")

    case "-":
        result= num1  - num2
        print(f"the result of {num1} - {num2} is {result}")

    case "*" :
        result = num1  * num2
        print(f"the result of {num1} * {num2} is {result}")
    case "/" :
        if num2 == 0:
            print("Error : cannot diveide by zero")
        else :
            print(f"the result of {num1} / {num2} is {result}")
    case _:
        print("Invalid operition selected") 
