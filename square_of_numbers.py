
def squareOfNumbers(num):
    d = {}
    if(0<num<100):
        for i in range(1,num+1):
            d[i] = i*i
        return d
