import matplotlib.pyplot as plt
import numpy as np

import sys
sys.path.append('..')

import membership

#Antecedents
a1 = []


for i in np.arange(0,10,0.01):	
	a1.append(membership.triang(i,1,3,5))		



plt.figure(figsize=(6,3))

plt.plot(np.arange(0,10,0.01),a1, color='red', label="A")

alpha = 0.6
plt.axhline(y=alpha, color='black', linestyle='--')

plt.axvline(x=2.2, color='black', linestyle='--')
plt.axvline(x=3.8, color='black', linestyle='--')

plt.annotate('', xy=(2.2, -.08),xytext=(3.8,-.08),                     #draws an arrow from one set of coordinates to the other
            arrowprops=dict(arrowstyle='<->',facecolor='red'),   #sets style of arrow and colour
            annotation_clip=False)

plt.annotate(r'$\mathcal{X}_{A \geq B(y)}$',xy=(2.3,-.16),xytext=(2.3,-.16),               #Adds another annotation for the text that you want
            annotation_clip=False)

# plt.xlabel('$X$')

plt.xticks([])

plt.yticks([alpha], ['B(y)'])

plt.legend()

# plt.show()
plt.savefig("plot_subconj_A_B.png")