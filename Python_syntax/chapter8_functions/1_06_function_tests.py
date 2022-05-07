def city_country(city, country):
	print(f"{city.title()}, {country.title()}")

city_country('rio', 'brazil')
city_country('tokyo', 'japan')
city_country('london', 'england')

def make_album(artist_name, album_title, songs = None):
	if songs:
		album = {'name': artist_name, 'title': album_title, 'songs': songs}
	else:
		album = {'name': artist_name, 'title': album_title}
	return album

queen1 = make_album('queen', 'we will rock you')
print(queen1)
tswift = make_album('taylor swift', '22')
print(tswift)
lp1 = make_album('linkin park', 'hybrid theory')
print(lp1)
queen2 = make_album('queen', 'we will rock you', '22')
print(queen2)
tswift2 = make_album('taylor swift', '22', '11')
print(tswift2)
