import matplotlib.pyplot as plt
import numpy as np

import sys
sys.path.append('..')

import membership

#Antecedents
a1 = []


for i in np.arange(0,10,0.001):	
	a1.append(membership.crisp(i,6))		



plt.figure(figsize=(6,3))

plt.plot(np.arange(0,10,0.001),a1, color='red', label=r"$A'_{x'}$")

plt.xticks([6],[r"$x'$"])

plt.yticks([1],['1'])

plt.legend()

# plt.show()
plt.savefig('plot_crisp.png')