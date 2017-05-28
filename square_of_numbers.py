def squareOfNumbers(num):

    d = dict()
    if(num < 0):
        return "Negative not allowed"
    elif(num>100):
        return "Greater then 100 not allowed"
    else:
        for i in range(1,num+1):
            d[i] = i**2

    return d

print squareOfNumbers(10)
