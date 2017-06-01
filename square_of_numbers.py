def squareOfNumbers(x):
    d={}
    if 0<x<100:
        for k in range(1,x+1):
            d[k]=k*k
        return d
    #if 0<x<100:
    #    d = [k:k*k for k in range(1,x+1)]
    #return d

#n=input("Enter a number: ")
a = squareOfNumbers(5)
print a
