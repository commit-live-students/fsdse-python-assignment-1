def squareOfNumbers (n):
    if n <= 0 or n > 100:
        print "Input n should be greater than 0 and upto 100"
        return {}
    return {i:i*i for i in range(1,n+1)}

if __name__ == "__main__":
    print squareOfNumbers (5)
    print squareOfNumbers (0)
    print squareOfNumbers (100)
    print squareOfNumbers (101)
