def squareOfNumbers(n):
    if n<0 or n>100:
        return

    squareDict = {}
    for i in range(n+1):
        squareDict[i]= i*i

    return squareDict

print squareOfNumbers(5)
