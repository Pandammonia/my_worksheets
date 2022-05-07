import praw
import pandas as pd

reddit = praw.Reddit(client_id="7Nf7jTPKSNpxjBfqMAh38g",
	                 client_secret="zzoJjXGRcM3JfCpL76jwuzgjaIBLMQ",
	                 user_agent="Luke",
	                 username="Pandammonia",
	                 password="Pandora17")

posts = []
ufo_sub = reddit.subreddit('UFOs')
for post in ufo_sub.hot(limit=10):
	posts.append([post.title, post.url, post.num_comments, post.selftext, post.created])
posts = pd.DataFrame(posts,columns=['title', 'url', 'num_comments', 'selftext', 'created'])
print(posts)