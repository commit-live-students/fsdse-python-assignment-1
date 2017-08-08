def squareOfNumbers(number):
    dictionary = dict()
    for no in range(1, number + 1):
        dictionary[no] = no ** 2
    return dictionary
number = 5
print squareOfNumbers(number)
