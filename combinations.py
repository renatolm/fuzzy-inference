''' Combinations of rule bases and inference systems
#TODO improve documentation '''

def bks_conj(inp, ant, cons, tnorm, implication):
	output = []

	for j in range(len(cons)):
		mini=1

		for k in range(len(ant)):
			curr = implication(inp[k], tnorm(ant[k], cons[j]))				

			if curr<mini:
				mini = curr

		output.append(mini)

	return output


def bks_imp(inp, ant, cons, tnorm, implication):
	output = []

	for j in range(len(cons)):
		mini=1

		for k in range(len(ant)):
			curr = implication(inp[k], implication(ant[k], cons[j]))				

			if curr<mini:
				mini = curr

		output.append(mini)

	return output


def cri_conj(inp, ant, cons, tnorm, implication):
	output = []

	for j in range(len(cons)):
		maxi=0

		for k in range(len(ant)):
			curr = tnorm(inp[k], tnorm(ant[k], cons[j]))					

			if curr>maxi:
				maxi = curr

		output.append(maxi)			

	return output


def cri_imp(inp, ant, cons, tnorm, implication):
	output = []

	for j in range(len(cons)):
		maxi=0

		for k in range(len(ant)):
			curr = tnorm(inp[k], implication(ant[k], cons[j]))					

			if curr>maxi:
				maxi = curr

		output.append(maxi)			

	return output