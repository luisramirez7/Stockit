import csv
import os
import datetime as dt

import pandas as pd
dates = pd.read_csv('prices.csv', usecols=[1,1])
thePandaArray = dates['date']
def isodateConverter(pandasArray, columnName):
	a = dates[columnName]
	new_column = []

	for pussy in a: 
		nicedate = pussy.split('-')
		year = nicedate[0]
		month = nicedate[1]
		day = nicedate[2]
		yearInt = int(year)
		monthInt = int(month)
		dayInt = int(day)
		numberedWeekday = dt.date(yearInt,monthInt,dayInt).isoweekday()
		new_column.append(numberedWeekday)

	dates["numbered_weekday"] = new_column

isodateConverter(thePandaArray, 'date')
