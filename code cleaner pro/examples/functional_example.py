# Before functional conversion
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = []

for num in numbers:
    if num % 2 == 0:
        even_squares.append(num ** 2)

print(even_squares)