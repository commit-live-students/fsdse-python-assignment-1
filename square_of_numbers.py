def squareOfNumbers(n):
    dictionary =dict()
    if n <= 100:
        for i in range(1,n+1):
            dictionary[i] = i**2
        return dictionary


n = input('Enter n :')

print squareOfNumbers(n)
