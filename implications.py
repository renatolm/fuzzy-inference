''' Collection of implication functions
#TODO improve documentation '''

def godel(x, y):
	if x<=y:
		return 1
	else:
		return y

def goguen(x, y):
	if x<=y:
		return 1
	else:
		return y/x
    
def lukasiewicz(x,y):
    return min(1,y-x+1)