users = {
	'einstein': {
	'first':'albert',
	'last':'einstein',
	'location':'princeton',
	},
	'mercury':{
	'first':'freddie',
	'last':'mercury',
	'location':'nyc',
	}
}

for username, info in users.items():
	print(f"\nUsername: {username.title()}")
	fullname = f"{info['first']} {info['last']}"
	location = info['location']
	print(f"\t Full name: {fullname.title()}")
	print(f"\t Location: {location.title()}")

