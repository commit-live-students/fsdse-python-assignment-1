
def squareOfNumbers(n):
    dict = {}
    if(n > 0  and n < 100):
        for i in range(1,n+1):
            dict[i] = i*i

    return dict

squareOfNumbers(0)
