def make_album(artist_name, album_title, songs = None):
	if songs:
		album = {'name': artist_name, 'title': album_title, 'songs': songs}
	else:
		album = {'name': artist_name, 'title': album_title}
	return album

while True:
	print("Please give me a singers name and album title")
	print("\nEnter 'leave' whenever to quit")
	a_name = input("Artists name: ")
	if a_name == 'leave':
		break
	a_title = input("Album title: ")
	if a_title == 'leave':
		break
	artalb = make_album(a_name, a_title)
	print(artalb)