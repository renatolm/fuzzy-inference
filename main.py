import numpy as np
import membership
import tnorms
import implications
from experiment import Experiment

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
	a1.append(membership.triang(i,1,3,5))
	a2.append(membership.triang(i,3,5,7))
	a3.append(membership.triang(i,5,7,9))		
# 	a1.append(membership.triang(i,1,4,7))
	# a1.append(membership.triang(i,1,3,5))

# 	b1.append(membership.triang(i,1,3,5))
	b1.append(membership.triang(i,1,2,3))
# 	b2.append(membership.triang(i,3.5,5.5,7.5))
	b2.append(membership.triang(i,3,4,5))
# 	b3.append(membership.triang(i,7,8,9))
	b3.append(membership.triang(i,5,6,7))

# 	inp.append(membership.triang(i,2,3,4))		
# 	inp.append(membership.triang(i,0,0.5,1))	
# 	inp.append(membership.triang(i,4,5,6))	
	inp.append(membership.crisp(i, 3.5))
# 	inp.append(membership.triang(i,2.5,3.5,4.5))

# for j in range(len(a1)):
# 	if a1[j]<0.3:
# 		a1[j]=0.3
# 	if inp[j]<0.2:
# 		inp[j]=0.2

antecedents = [a1,a2,a3]
# antecedents = [a1]
consequents = [b1,b2,b3]
# consequents = [b1]

# name = "exp5"
name = "exp40"
description = "detailed exp with crisp input"
# description = "same as exp5 but with product tnorm and goguen implication"
# description = "same as exp7, input included in the antecedent but both with all values above 0"
# description = "same as exp4 but with fuzzy input"
# description = "same as exp11 but with product tnorm and goguen implication"
tnorm = tnorms.minimum
# tnorm = tnorms.product
# tnorm = tnorms.lukasiewicz
implication = implications.godel
# implication = implications.goguen
# implication = implications.lukasiewicz

# experiment = Experiment(name, description, inp, a1, b1, tnorm, implication)
experiment = Experiment(name, description, inp, antecedents, consequents, tnorm, implication)

# experiment.run_full_experiment(detailed=True, beta=True, inputs=True)
experiment.run_full_experiment(detailed=True, beta=False, inputs=False)