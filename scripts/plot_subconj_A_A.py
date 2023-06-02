import matplotlib.pyplot as plt
import numpy as np

import sys
sys.path.append('..')

import membership


a1 = []
a2 = []


for i in np.arange(0,10,0.01):	
	a1.append(membership.triang(i,1,3,5))		
	a2.append(membership.triang(i,3.5,4.5,5.5))


plt.figure(figsize=(6,3))

plt.plot(np.arange(0,10,0.01),a1, color='red', label="A")
plt.plot(np.arange(0,10,0.01),a2, color='blue', label="B")

plt.axvline(x=4, color='black', linestyle='--')
plt.axvline(x=5.5, color='black', linestyle='--')

plt.annotate('', xy=(4, -.08),xytext=(5.5,-.08),                     #draws an arrow from one set of coordinates to the other
            arrowprops=dict(arrowstyle='<->',facecolor='red'),   #sets style of arrow and colour
            annotation_clip=False)

plt.annotate(r'$\mathcal{X}_{A<B}$',xy=(4.1,-.16),xytext=(4.1,-.16),               #Adds another annotation for the text that you want
            annotation_clip=False)

# plt.xlabel('$X$')

plt.xticks([])
plt.yticks([])

plt.legend()

# plt.show()

plt.savefig("plot_subconj_A_A.png")