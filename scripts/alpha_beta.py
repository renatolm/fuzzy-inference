'''Script to calculate alpha and beta given
	an input and a fuzzy rule base'''

import numpy as np

import sys
sys.path.append('..')

import membership
import implications
import tnorms

#Antecedents
a1 = []
a2 = []
a3 = []

#Consequents
b1 = []
b2 = []
b3 = []

#Input
inp = []

for i in np.arange(0,10,0.01):	
	# a1.append(membership.triang(i,1,3,5))
	# a2.append(membership.triang(i,3,5,7))
	# a3.append(membership.triang(i,5,7,9))		
	a1.append(membership.triang(i,1,4,7))
	# a1.append(membership.triang(i,1,3,5))

	b1.append(membership.triang(i,1,3,5))
	# b2.append(membership.triang(i,3.5,5.5,7.5))
	# b3.append(membership.triang(i,7,8,9))	

	inp.append(membership.triang(i,2,3,4))	
	# inp.append(membership.crisp(i, 3.5))

# tnorm = tnorms.minimum
tnorm = tnorms.product
# implication = implications.godel
implication = implications.goguen

alpha = 0
beta = 1
for x in range(len(a1)):
	curr_alpha = tnorm(inp[x], a1[x])
	curr_beta = implication(inp[x], a1[x])

	if curr_alpha>alpha:
		alpha = curr_alpha

	if curr_beta<beta:
		beta = curr_beta

print("alpha = {}".format(alpha))
print("beta = {}".format(beta))