def squareOfNumbers(n):
    square_of_numbers = {}
    for i in range(1, n+1):
        square = i*i
        square_of_numbers[i] = square
    return square_of_numbers
