'''
The aim of this script is to verify if the combination BKS+conj is equivalent to
Infimum(\beta_i * B_i)
'''

import sys
sys.path.append('..')

import membership
import implications
import tnorms
import combinations
import plot

import numpy as np

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

for i in np.arange(0,10,0.001):	
	a1.append(membership.triang(i,1,3,5))
	a2.append(membership.triang(i,3,5,7))
	a3.append(membership.triang(i,5,7,9))		

	b1.append(membership.triang(i,1,3,5))
	b2.append(membership.triang(i,3.5,5.5,7.5))
	b3.append(membership.triang(i,7,8,9))	

	inp.append(membership.triang(i,2.5,3.5,4.5))

antecedents = [a1,a2,a3]
consequents = [b1,b2,b3]

# implication = implications.godel
implication = implications.goguen
# tnorm = tnorms.minimum
tnorm = tnorms.product

output_original = combinations.bks_conj(inp, antecedents, consequents, tnorm, implication)	
output_beta = combinations.bks_conj_beta(inp, antecedents, consequents, tnorm, implication)

print(all(np.equal(output_original,output_beta)))
plot.plot_outputs(output_original, consequents, "Original", filename_preffix=None)
plot.plot_outputs(output_beta, consequents, "Beta", filename_preffix=None)