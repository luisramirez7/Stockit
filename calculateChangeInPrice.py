import pandas as pd
import numpy as np

def changeInPrice(dataframe):
	numpyArray = dataframe.values
	close = numpyArray[:,4].astype('float')
	start = numpyArray[:,7].astype('float')
	change = (close - start) / start
	return np.append(numpyArray, change[:,None], axis = 1)