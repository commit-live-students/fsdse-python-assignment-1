def squareOfNumbers(n):
    if n<0 and n>100:
        print('enter no between 0-100')
        return 1

    dict1 = {}
    for i in range(1, n+1):
        dict1[i]=i**2
            #dict1.update({i: i ** 2})
    return dict1
