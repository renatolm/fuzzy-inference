from __future__ import division
import numpy as np
import warnings

def centroid_old(fuzzyOutput, ini, end, precision):
	num = 0
	den = 0
	i = 0

	for k in np.arange(ini, end, precision):
		num = num + (k*fuzzyOutput[i])
		den = den + fuzzyOutput[i]

		i = i + 1

	with warnings.catch_warnings():
		warnings.filterwarnings('error')
		try:
			return num/den	
		except RuntimeWarning:
			#print fuzzyOutput
			#print "num: "+str(num)+" den: "+str(den)
			#print "problemas"
			return 0
        
def centroid(output, interval):
    num = 0
    den = 0
    
    for i, y in enumerate(interval):
        num = num + (y*output[i])
        den = den + output[i]
        
    with warnings.catch_warnings():
        warnings.filterwarnings('error')
        try:
            return num/den	
        except RuntimeWarning:
			#print fuzzyOutput
			#print "num: "+str(num)+" den: "+str(den)
			#print "problemas"
            return 0
        
def mom(output, interval):
    
    maxima = 0
    maxima_arr = []
    
    for i, y in enumerate(interval):
        if output[i]>maxima:
            maxima = output[i]
            maxima_arr = [y]
        elif output[i]==maxima:
            maxima_arr.append(y)
            
    return np.mean(maxima_arr)