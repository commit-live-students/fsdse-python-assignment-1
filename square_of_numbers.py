def squareOfNumbers(x):
    d={}
    if 0<x<100:
        for k in range(1,x+1):
            d[k]=k**2
        return d
a = squareOfNumbers(3)
print a
