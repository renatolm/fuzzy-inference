from __future__ import division
import numpy as np

''' Collection of membership functions
#TODO improve documentation '''

def triang(x, begin, top, end):
	if (x > begin) and (x < top):
		return (x / (top - begin)) - (begin / (top - begin))
	elif (x > top) and (x < end):
		return (-x / (end - top)) + (end / (end - top))
	elif x == top:
		return 1
	else:
		return 0

def trap(x, begin, top1, top2, end):
	if (x > begin) and (x < top1):
		return (x / (top1 - begin)) - (begin / (top1 - begin))
	elif (x > top2) and (x < end):
		return (-x / (end - top2)) + (end / (end - top2))
	elif (x >= top1) and (x <= top2):
		return 1
	else:
		return 0

def inf_border(x, top, end):
	if x <= top:
		return 1
	elif (x > top) and (x <end):
		return (-x / (end - top)) + (end / (end - top))
	else:
		return 0

def sup_border(x, begin, top):
	if x <= begin:
		return 0
	elif (x > begin) and (x < top):
		return (x / (top - begin)) - (begin / (top - begin))
	else:
		return 1

def gaussian(x, mu, sig):
	return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))

def alpha_cut_triang(alpha, begin, top, end):
	cut = []
	for i in np.arange(begin, end, 0.1):
		if triang(i, begin, top, end) >= alpha:
			cut.append(i)

	return cut

def alpha_cut_trap(alpha, begin, top1, top2, end):
	cut = []
	for i in np.arange(begin, end, 0.1):
		if trap(i, begin, top1, top2, end) >= alpha:
			cut.append(i)

	return cut

def crisp(x, top):
	if x == top:
		return 1
	else:
		return 0