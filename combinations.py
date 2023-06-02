''' Combinations of rule bases and inference systems
#TODO improve documentation '''

import numpy as np

def bks_conj(inp, antecedents, consequents, tnorm, implication):
	output = []

	for j in range(len(consequents[0])):
		mini=1

		for k in range(len(antecedents[0])):
			rule_agg = 0
			for ant, cons in zip(antecedents, consequents):
				rule_agg = max(rule_agg, tnorm(ant[k], cons[j])) 

			curr = implication(inp[k], rule_agg)				

			if curr<mini:
				mini = curr

		output.append(mini)

	return output

def bks_conj_detailed_A_less_Ai(inp, antecedents, consequents, tnorm, implication):
	'''So far only works with one rule'''
	output = []

	for j in range(len(consequents[0])):
		mini=1

		for k in range(len(antecedents[0])):
			rule_agg = 0
			for ant, cons in zip(antecedents, consequents):
				rule_agg = max(rule_agg, tnorm(ant[k], cons[j])) 

			if inp[k]<=antecedents[0][k]:
				curr = implication(inp[k], rule_agg)				

				if curr<mini:
					mini = curr

		output.append(mini)

	return output


def bks_conj_detailed_A_greater_Ai(inp, antecedents, consequents, tnorm, implication):
	'''So far only works with one rule'''
	output = []

	for j in range(len(consequents[0])):
		mini=1

		for k in range(len(antecedents[0])):
			rule_agg = 0
			for ant, cons in zip(antecedents, consequents):
				rule_agg = max(rule_agg, tnorm(ant[k], cons[j])) 

			if inp[k]>antecedents[0][k]:
				curr = implication(inp[k], rule_agg)				

				if curr<mini:
					mini = curr

		output.append(mini)

	return output


def bks_conj_detailed_inputs(inp, antecedents, consequents, tnorm, implication):
	'''So far only works with one rule'''
	inp_detailed = []
	ant_detailed = []
	output = []

	for j in range(len(consequents[0])):
		mini=1
		curr_inp=0
		curr_ant=0

		for k in range(len(antecedents[0])):
			rule_agg = 0
			for ant, cons in zip(antecedents, consequents):
				rule_agg = max(rule_agg, tnorm(ant[k], cons[j])) 

			curr = implication(inp[k], rule_agg)				

			if curr<mini:
				curr_inp = inp[k]
				curr_ant = antecedents[0][k]
				mini = curr

		output.append(mini)
		inp_detailed.append(curr_inp)
		ant_detailed.append(curr_ant)

	return output, inp_detailed, ant_detailed


def bks_conj_detailed_beta(inp, antecedents, consequents, tnorm, implication):
	'''So far only works with one rule'''
	beta = 1	
	for k in range(len(antecedents[0])):
		curr_beta = implication(inp[k], antecedents[0][k])
		beta = min(beta, curr_beta)	

	output = []

	for j in range(len(consequents[0])):
		
		output.append(tnorm(beta, consequents[0][j]))

	return output, beta


def bks_conj_beta(inp, antecedents, consequents, tnorm, implication):
	# output = np.ones_like(consequents[0])
	output = np.zeros_like(consequents[0])

	for i in range(len(antecedents)):
		beta = 1	
		if all(np.less_equal(inp, antecedents[i])):
			curr_output = consequents[i]
		else:
			for k in range(len(antecedents[i])):
				curr_beta = implication(inp[k], antecedents[i][k])
				beta = min(beta, curr_beta)	

			curr_output = []

			for j in range(len(consequents[i])):
				
				curr_output.append(tnorm(beta, consequents[i][j]))

		# output = np.minimum(output, curr_output)
		output = np.maximum(output, curr_output)

	return output


def bks_conj_detailed_A_less_Bi(inp, antecedents, consequents, tnorm, implication):
	'''So far only works with one rule'''
	output = []

	for j in range(len(consequents[0])):
		mini=1

		for k in range(len(antecedents[0])):
			rule_agg = 0
			for ant, cons in zip(antecedents, consequents):
				rule_agg = max(rule_agg, tnorm(ant[k], cons[j])) 

			if inp[k]<=consequents[0][j]:
				curr = implication(inp[k], rule_agg)				

				if curr<mini:
					mini = curr

		output.append(mini)

	return output


def bks_conj_detailed_A_greater_Bi(inp, antecedents, consequents, tnorm, implication):
	'''So far only works with one rule'''
	output = []

	for j in range(len(consequents[0])):
		mini=1

		for k in range(len(antecedents[0])):
			rule_agg = 0
			for ant, cons in zip(antecedents, consequents):
				rule_agg = max(rule_agg, tnorm(ant[k], cons[j])) 

			if inp[k]>consequents[0][j]:
				curr = implication(inp[k], rule_agg)				

				if curr<mini:
					mini = curr

		output.append(mini)

	return output


def bks_imp(inp, antecedents, consequents, tnorm, implication):
	output = []

	for j in range(len(consequents[0])):
		mini=1

		for k in range(len(antecedents[0])):
			rule_agg = 1
			for ant, cons in zip(antecedents, consequents):
				rule_agg = min(rule_agg, implication(ant[k], cons[j]))

			curr = implication(inp[k], rule_agg)				

			if curr<mini:
				mini = curr

		output.append(mini)

	return output


def bks_imp_detailed_inputs(inp, antecedents, consequents, tnorm, implication):
	'''So far only works with one rule'''
	output = []
	inp_detailed = []
	ant_detailed = []

	for j in range(len(consequents[0])):
		mini=1
		curr_inp = 0
		curr_ant = 0

		for k in range(len(antecedents[0])):
			rule_agg = 1
			for ant, cons in zip(antecedents, consequents):
				rule_agg = min(rule_agg, implication(ant[k], cons[j]))

			curr = implication(inp[k], rule_agg)				

			if curr<mini:
				mini = curr
				curr_inp = inp[k]
				curr_ant = antecedents[0][k]

		output.append(mini)
		inp_detailed.append(curr_inp)
		ant_detailed.append(curr_ant)

	return output, inp_detailed, ant_detailed


def cri_conj(inp, antecedents, consequents, tnorm, implication):
	output = []

	for j in range(len(consequents[0])):
		maxi=0

		for k in range(len(antecedents[0])):
			rule_agg = 0
			for ant, cons in zip(antecedents, consequents):
				rule_agg = max(rule_agg, tnorm(ant[k], cons[j]))

			curr = tnorm(inp[k], rule_agg)					

			if curr>maxi:
				maxi = curr

		output.append(maxi)			

	return output


def cri_conj_detailed_inputs(inp, antecedents, consequents, tnorm, implication):
	'''So far only works with one rule'''
	output = []
	inp_detailed = []
	ant_detailed = []

	for j in range(len(consequents[0])):
		maxi=0
		curr_inp = 0
		curr_ant = 0

		for k in range(len(antecedents[0])):
			rule_agg = 0
			for ant, cons in zip(antecedents, consequents):
				rule_agg = max(rule_agg, tnorm(ant[k], cons[j]))

			curr = tnorm(inp[k], rule_agg)					

			if curr>maxi:
				maxi = curr
				curr_inp = inp[k]
				curr_ant = antecedents[0][k]

		output.append(maxi)			
		inp_detailed.append(curr_inp)
		ant_detailed.append(curr_ant)

	return output, inp_detailed, ant_detailed


def cri_imp(inp, antecedents, consequents, tnorm, implication):
	output = []

	for j in range(len(consequents[0])):
		maxi=0

		for k in range(len(antecedents[0])):
			rule_agg = 1
			for ant, cons in zip(antecedents, consequents):
				rule_agg = min(rule_agg, implication(ant[k], cons[j]))

			curr = tnorm(inp[k], rule_agg)					

			if curr>maxi:
				maxi = curr

		output.append(maxi)			

	return output


def cri_imp_detailed_A_less_Ai(inp, antecedents, consequents, tnorm, implication):
	'''So far only works with one rule'''
	output = []

	for j in range(len(consequents[0])):
		maxi=0

		for k in range(len(antecedents[0])):
			rule_agg = 1
			for ant, cons in zip(antecedents, consequents):
				rule_agg = min(rule_agg, implication(ant[k], cons[j])) 

			if inp[k]<=antecedents[0][k]:
				curr = tnorm(inp[k], rule_agg)				

				if curr>maxi:
					maxi = curr

		output.append(maxi)

	return output


def cri_imp_detailed_A_greater_Ai(inp, antecedents, consequents, tnorm, implication):
	'''So far only works with one rule'''
	output = []

	for j in range(len(consequents[0])):
		maxi=0

		for k in range(len(antecedents[0])):
			rule_agg = 1
			for ant, cons in zip(antecedents, consequents):
				rule_agg = min(rule_agg, implication(ant[k], cons[j])) 

			if inp[k]>antecedents[0][k]:
				curr = tnorm(inp[k], rule_agg)				

				if curr>maxi:
					maxi = curr

		output.append(maxi)

	return output


def cri_imp_detailed_A_less_Bi(inp, antecedents, consequents, tnorm, implication):
	'''So far only works with one rule'''
	output = []

	for j in range(len(consequents[0])):
		maxi=0

		for k in range(len(antecedents[0])):
			rule_agg = 1
			for ant, cons in zip(antecedents, consequents):
				rule_agg = min(rule_agg, implication(ant[k], cons[j])) 

			if inp[k]<=consequents[0][j]:
				curr = tnorm(inp[k], rule_agg)				

				if curr>maxi:
					maxi = curr

		output.append(maxi)

	return output


def cri_imp_detailed_A_greater_Bi(inp, antecedents, consequents, tnorm, implication):
	'''So far only works with one rule'''
	output = []

	for j in range(len(consequents[0])):
		maxi=0

		for k in range(len(antecedents[0])):
			rule_agg = 1
			for ant, cons in zip(antecedents, consequents):
				rule_agg = min(rule_agg, implication(ant[k], cons[j])) 

			if inp[k]>consequents[0][j]:
				curr = tnorm(inp[k], rule_agg)				

				if curr>maxi:
					maxi = curr

		output.append(maxi)

	return output


def cri_imp_detailed_Ai_less_Bi(inp, antecedents, consequents, tnorm, implication):
	'''So far only works with one rule'''
	output = []

	for j in range(len(consequents[0])):
		maxi=0

		for k in range(len(antecedents[0])):
			rule_agg = 1
			for ant, cons in zip(antecedents, consequents):
				rule_agg = min(rule_agg, implication(ant[k], cons[j])) 

			if antecedents[0][k]<=consequents[0][j]:
				curr = tnorm(inp[k], rule_agg)				

				if curr>maxi:
					maxi = curr

		output.append(maxi)

	return output


def cri_imp_detailed_Ai_greater_Bi(inp, antecedents, consequents, tnorm, implication):
	'''So far only works with one rule'''
	output = []

	for j in range(len(consequents[0])):
		maxi=0

		for k in range(len(antecedents[0])):
			rule_agg = 1
			for ant, cons in zip(antecedents, consequents):
				rule_agg = min(rule_agg, implication(ant[k], cons[j])) 

			if antecedents[0][k]>consequents[0][j]:
				curr = tnorm(inp[k], rule_agg)				

				if curr>maxi:
					maxi = curr

		output.append(maxi)

	return output


def cri_imp_detailed_beta(inp, antecedents, consequents, tnorm, implication):
	'''So far only works with one rule'''
	beta = 1
	for k in range(len(antecedents[0])):
		curr_beta = implication(inp[k], antecedents[0][k])
		beta = min(beta, curr_beta)	

	output = []

	for j in range(len(consequents[0])):
		
		output.append(implication(beta, consequents[0][j]))

	return output, beta


def cri_imp_detailed_inputs(inp, antecedents, consequents, tnorm, implication):
	'''So far only works with one rule'''
	output = []
	inp_detailed = []
	ant_detailed = []

	for j in range(len(consequents[0])):
		maxi=0
		curr_inp=0
		curr_ant=0

		for k in range(len(antecedents[0])):
			rule_agg = 1
			for ant, cons in zip(antecedents, consequents):
				rule_agg = min(rule_agg, implication(ant[k], cons[j]))

			curr = tnorm(inp[k], rule_agg)					

			if curr>maxi:
				maxi = curr
				curr_inp = inp[k]
				curr_ant = antecedents[0][k]

		output.append(maxi)			
		inp_detailed.append(curr_inp)
		ant_detailed.append(curr_ant)

	return output, inp_detailed, ant_detailed