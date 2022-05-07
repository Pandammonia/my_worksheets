import praw
import pandas as pd

reddit = praw.Reddit(client_id="7Nf7jTPKSNpxjBfqMAh38g",
	                 client_secret="zzoJjXGRcM3JfCpL76jwuzgjaIBLMQ",
	                 user_agent="Luke",
	                 username="Pandammonia",
	                 password="Pandora17")

hot_posts = reddit.subreddit('Dogman').hot(limit=10) # .top(), .hot()
print("_---------Posts from r/Dogman---------")
for post in hot_posts:
        print(post.title)

print("-----------------------------------------------------")
print("\n\n")
print("-----Posts from UFO subreddit-----")

hot_posts = reddit.subreddit('Ufos').hot(limit=10) # .top(), .hot()
for post in hot_posts:
	print(post.title)
