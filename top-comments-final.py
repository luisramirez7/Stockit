import praw

reddit = praw.Reddit(client_id='YOURCLIENTID',
                     client_secret='YOURCLIENTSECRET',
                     password='YOURPASSWORD',
                     user_agent='testscript by /u/fakebot3',
                     username='YOURUSERNAME')

baidu = []
baiduScore = []
facebook = []
facebookScore = []
microsoft = []
microsoftScore = []


for submission in reddit.subreddit('investing+AMD_Stock+StockMarket').submissions(1426837664, 1489996064):

	title = submission.title
	updoots = submission.score

	agnosticTitles = str(title).lower()
	# verylargdic = dict(*zip(agnosticTitles, updoots))
	if "baidu" in agnosticTitles:
		baidu.append(title)
		baiduScore.append(updoots)
	if "facebook" in agnosticTitles:
		facebook.append(title)
		facebookScore.append(updoots)
	if "microsoft" in agnosticTitles: 
		microsoft.append(title)
		microsoftScore.append(updoots)


print(baidu, facebook, microsoft)
	# if any("baidu" in key for key in verylargdic):
	# 	baidu.append(submission.title)
	# 	baiduScore.append(submission.score)
	# if any("facebook" in key for key in verylargdic): 
	# 	facebook.append(submission.title)
	# 	facebookScore.append(submission.score)
	# if any("microsoft" in key for key in verylargdic):
	# 	microsoft.append(submission.title)
	# 	microsoftScore.append(submission.score)

# testDict = {"baidu sucks ass" : 234, "microsoft sucks ass" : 273}
# if any("baidu" in key for key in testDict):
# 	print(testDict["baidu sucks ass"])
