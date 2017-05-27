dect = {}

def squareOfNumbers(n):
    if (n>100): n=100

    for x in range(1,n):
        dect = {row : row*row for row in range(1,n+1)}

    return dect

print squareOfNumbers(11)
