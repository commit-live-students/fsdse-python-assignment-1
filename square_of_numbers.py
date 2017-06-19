# Generate a dictionary that contains (i, i*i)



# def get_n():
#     n = int(raw_input("N: "))
#     if (n<0 or n>100):
#         get_n()
#     else:
#         return n

# k = get_n()

def squareOfNumbers(k):
    dict_eg = {}
    for i in range(1,k+1):
        dict_eg[i] = i*i

    return dict_eg

squareOfNumbers(10)

#Done, Not posted=======================================================================================
