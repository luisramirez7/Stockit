import os
import tarfile
tonsofdata = "tonsofdata"
def unTarMe(fileDirectory):
	for filename in os.listdir('/Users/luis/Documents/hackingstuff/hack-stock/tonsofdata'):
		extension = os.path.splitext(filename)[1]
		prefix = os.path.splitext(filename)[0]
		if extension == ".gz":
			tar = tarfile.open("/Users/luis/Documents/hackingstuff/hack-stock/tonsofdata/" + filename)
			tar.extractall(path="/Users/luis/Documents/hackingstuff/hack-stock/tonsofdata/" + prefix)
			tar.close()

unTarMe(tonsofdata)