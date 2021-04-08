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