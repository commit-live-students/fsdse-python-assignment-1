#def squareOfNumbers(n):
#    print {i:i*i for i in range(n+1)}
#
#squareOfNumbers(100)

def squareOfNumbers(n):
    dict1 = {}
    for i in range(n+1):
        dict1.update({i:i*i})
    return dict1

squareOfNumbers(5)
