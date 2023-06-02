''' Collection of t-norms functions
#TODO improve documentation '''

def minimum(x,y):
	return min(x,y)

def product(x,y):
	return x*y

def lukasiewicz(x,y):
    return max(0,x+y-1)