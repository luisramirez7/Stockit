import pandas as pd

def mergeCsvOnSymbol(file1, file2):
	df1 = pd.read_csv(file1)
	df2 = pd.read_csv(file2)
	result = pd.merge(df1, df2, on="symbol", how="inner")
	return result
