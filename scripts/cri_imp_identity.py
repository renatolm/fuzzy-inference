'''
The aim of this script is to verify if the identity
x * (y -> z) =  y -> (x*z)
is true
'''

import numpy as np

import sys
sys.path.append('..')

import membership
import implications
import tnorms

x_arr = np.arange(0,1,0.1)
y_arr = np.arange(0,1,0.1)
z_arr = np.arange(0,1,0.1)

implication = implications.godel
# implication = implications.goguen
tnorm = tnorms.minimum
# tnorm = tnorms.product

for x in x_arr:
	for y in y_arr:
		for z in z_arr:
			left_term = tnorm(x,implication(y,z))
			# right_term = tnorm(x,implication(y,tnorm(x,z)))
			# right_term = implication(y,tnorm(x,z)) 	# from Peter
			right_term = tnorm(implication(y,x),z) 	# derived from Peter
			# right_term = tnorm(implication(y, x),z)
			# right_term = implication(tnorm(y,x),z)

			if y>z:	# this is the right condition!
				if round(left_term,2) != round(right_term,2):
					print("Left term: {}".format(left_term))
					print("Right term: {}".format(right_term))
					print("x: {}\ty: {}\tz: {}\n".format(x,y,z))
					break
			else:
				pass