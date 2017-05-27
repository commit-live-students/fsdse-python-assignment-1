def squareOfNumbers(number):
    d={}
    for i in range(1,number+1):
        d[i]=i*i
    return d

print squareOfNumbers(100)
