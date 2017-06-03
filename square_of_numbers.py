n=0
a = {}
def squareOfNumbers(n):

	if(n<101) and (n>=0):
		a = {x: x*x for x in range(0,n+1)}
		return a

	else:
		print "Out of bounds"

squareOfNumbers(10)
