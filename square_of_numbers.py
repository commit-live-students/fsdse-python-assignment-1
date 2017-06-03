def squareOfNumbers(x):
#    d=dict()
    d={}
    if x >= 0 and x <= 100:
        for i in range(1,x+1):
            d.update ({i:i**2})
        return d
        print d
    else:
        print "Out of range"
print squareOfNumbers(2)
