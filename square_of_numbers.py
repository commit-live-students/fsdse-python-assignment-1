def squareOfNumbers(n):
    data = {}
    for i in range(n+1):
        data[i] = i*i
    return data

print squareOfNumbers(8)
