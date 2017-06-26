def  squareOfNumbers(num):
    t = {}
    if num > 0 and num <= 100:
        for x in range(1,num+1):
            t.update({x: pow(x, 2)})
    return t
