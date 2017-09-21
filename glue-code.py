from mergeCsvOnSymbol import *
from date_to_day_and_month import *
from calculateChangeInPrice import *
from sentiment import *
import pandas as pd
import os
import tarfile

tonsofdata = "tonsofdata"
superempty = "/Users/luis/Documents/hackingstuff/hack-stock/superempty"

def unTarMe(fileDirectory):
	for filename in os.listdir('/Users/luis/Documents/hackingstuff/hack-stock/tonsofdata'):
		extension = os.path.splitext(filename)[1]
		prefix = os.path.splitext(filename)[0]
		if extension == ".gz":
			tar = tarfile.open("/Users/luis/Documents/hackingstuff/hack-stock/tonsofdata/" + filename)
			tar.extractall(path="/Users/luis/Documents/hackingstuff/hack-stock/tonsofdata/" + prefix)
			tar.close()


def final_data(folderdirectory):
	industries_filepath = "/Users/luis/Documents/hackingstuff/hack-stock/industries.csv"
	for foldername in os.listdir(folderdirectory):
		if foldername==".DS_Store" or foldername=="tonsofdata20161010.tar":
			continue
		prices_filepath = "/Users/luis/Documents/hackingstuff/hack-stock/superempty/" + foldername + "/prices.csv"
		output = mergeCsvOnSymbol(file1=industries_filepath, file2=prices_filepath)
		dateInputForLooE = output["date"]
		date_add = isodateConverter(dateInputForLooE, 0)
		output["weekday"] = date_add
		final_data_clean = changeInPrice(output)
		sentimentData = sentiment('redditposts.txt')
		final_data_clean = pd.merge(final_data_clean, sentimentData, on="data", how="inner")
		print(final_data_clean)
	return(final_data_clean)	
final_data(superempty)