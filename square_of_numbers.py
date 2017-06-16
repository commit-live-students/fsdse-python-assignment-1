def squareOfNumbers(n):
    d={}
    if n<0 or n>100:
        print "The number is less than zero or more than 100"
    else:
        for i in range(1,n+1):
            d[i]=i*i
    return d
