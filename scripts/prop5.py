'''
The aim of this script is to verify if
x -> (y*z) >= (x -> y)*z
is true for every x,y,z in [0,1]
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
tnorm = tnorms.minimum

for x in x_arr:
	for y in y_arr:
		for z in z_arr:
			left_term = implication(x,tnorm(y,z))
			right_term = tnorm(implication(x,y),z)

			
			if left_term < right_term:
				print("Left term: {}".format(left_term))
				print("Right term: {}".format(right_term))
				print("x: {}\ty: {}\tz: {}\n".format(x,y,z))
				# break			