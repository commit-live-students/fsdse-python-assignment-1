def squareOfNumbers(n):
    dt = {}
    for i in range(1,n+1):
        dt.update({i:i*i})
    return dt

squareOfNumbers(5)
