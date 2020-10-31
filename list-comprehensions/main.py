# -----------------------------------------
prizes = [5, 10, 50, 100, 200]

double_prizes = []

for prize in prizes:
    double_prizes.append(prize * 2)

print(double_prizes)

double_prizes = [prize * 2 for prize in prizes]
print(double_prizes)
# -----------------------------------------
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square_even_numbers = []

for number in numbers:
    if number % 2 == 0:
        square_even_numbers.append(number ** 2)
print(square_even_numbers)

square_even_numbers = [number ** 2 for number in numbers if number % 2 == 0]
print(square_even_numbers)
# -----------------------------------------
