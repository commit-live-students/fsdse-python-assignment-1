
def squareOfNumbers(number):
    if number < 0 or number > 100:
        return
    squares = {}
    for i in range(1, number + 1):
        squares[i] = i*i

    return squares
