number = 1
sum = 0
print("Enter a number. Please enter zero(0) to exit")

while number != 0:
    number = float(input("Number: "))
    sum = sum + number
    print("Sum = ", sum)

else:
    print("Total Sum = ", sum)
