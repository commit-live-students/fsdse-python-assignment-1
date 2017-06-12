def squareOfNumbers(num):
    dict = {}
    if(num in range(0, 101)):
        for i in range(1, num+1):
           squar = i * i
           dict[i] = squar
           i += 1
    return dict


print squareOfNumbers(10)


# {1:1, 2:4, 3:9}
