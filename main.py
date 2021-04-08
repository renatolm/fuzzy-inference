import numpy as np
import membership
import tnorms
import implications

#Antecedents
a1 = []

#Consequents
b1 = []

#Input
inp = []

for i in np.arange(0,10,0.01):	
	a1.append(membership.triang(i,1,4,7))		

	b1.append(membership.triang(i,1,3,5))			

	inp.append(membership.triang(i,2,3,4))	