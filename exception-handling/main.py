number1 = float(input("Enter number 1: "))
number2 = float(input("Enter number 2: "))

try:
    result = number1 / number2
    print("Result = ",result)
except ZeroDivisionError as exception:
    print("Error: ", exception)

print("End")

