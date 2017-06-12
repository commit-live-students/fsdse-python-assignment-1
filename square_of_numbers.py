def squareOfNumbers(n=1):
    dict1 = {}
    if n > 0 and n < 100:
        for i in range(1, n+1):
            dict1.update({i: i**2})
        return dict1
    else:
        print("Invalid input, enter number between 0 to 100")
        pass
