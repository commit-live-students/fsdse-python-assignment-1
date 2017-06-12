def squareOfNumbers(n):
    squares = {}
    if n <0  or n>100:
        return
    for i in range(1,n+1):
        squares[i] = i*i
    return squares
