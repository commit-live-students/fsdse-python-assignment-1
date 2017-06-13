def squareOfNumbers(n):
    d={}
    i=1
    while(i<=n):
        d[i]=i**2
        i=i+1
    return d

print squareOfNumbers(5)    
