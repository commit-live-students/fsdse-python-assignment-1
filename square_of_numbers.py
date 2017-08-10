def squareOfNumbers(n):
    output = {}
    for i,v in enumerate(range(1, n + 1)):
        output[i + 1] = v ** 2
    return output


if __name__ == '__main__':
    print squareOfNumbers(5)
