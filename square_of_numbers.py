def squareOfNumbers(num):
    dict = {}
    if num > 0 and num <= 100:
        for a in range(1, num+1):
            dict.update({a:pow(a,2)})
    return dict
