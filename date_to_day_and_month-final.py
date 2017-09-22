import csv
import os
import datetime as dt

import pandas as pd

def isodateConverter(pandasArray, columnNumber):
	a = pandasArray
	new_column = []

	for poorlyformattedDates in a: 
		nicedate = poorlyformattedDates.split('-')
		year = nicedate[0]
		month = nicedate[1]
		day = nicedate[2]
		yearInt = int(year)
		monthInt = int(month)
		dayInt = int(day)
		numberedWeekday = dt.date(yearInt,monthInt,dayInt).isoweekday()
		new_column.append(numberedWeekday)

	# pandasArray["numbered_weekday"] = new_column
	return new_column