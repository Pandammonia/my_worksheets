
import requests
from plotly.graph_objs import Bar
from plotly import offline

subreddit = 'dogman'
limit = 100
timeframe = 'month' #hour, day, week, month, year, all
listing = 'top' # controversial, best, hot, new, random, rising, top

def get_reddit (subreddit, listing, limit, timeframe):
	try:
		base_url = f'https://www.reddit.com/r/{subreddit}/{listing}.json?limit={limit}&t={timeframe}'
		request = requests.get(base_url, headers = {'User-agent': 'yourbot'})
	except:
		print('An Error Occured')
	return request.json()

dict = get_reddit('dogman','top',100,'all')
df = pd.DataFrame(dict)
  
# displaying the DataFrame
display(df)