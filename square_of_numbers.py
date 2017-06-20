
def squareOfNumbers(num) :
    dictY = {}
    if (num > 0 and num < 100) :
        for i in range(1,num+1):
            dictY[i]=i*i
    else :
        print ("Please enter the input between 0 to 100!")
    return (dictY)


#num = int( input("Input a number ") )
squareOfNumbers(5)
