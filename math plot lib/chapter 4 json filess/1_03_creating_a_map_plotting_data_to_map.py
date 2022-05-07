import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

#Explore structure of data
filename = 'data/eq_data_30_day_m1.json' #open json file as filename
with open(filename) as f:
	all_eq_data = json.load(f) #store all data in all eq data

all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts)) 

mags, lons, lats, hovertexts = [], [], [], [] 
for eq_dict in all_eq_dicts: #create loop for all of our data
	mag = eq_dict['properties']['mag'] #magnitude is under each dictioanry in [properties] [mag]
	lon = eq_dict['geometry']['coordinates'][0]
	lat = eq_dict['geometry']['coordinates'][1]
	title = eq_dict['properties']['title']
	mags.append(mag)
	lons.append(lon)
	lats.append(lat)
	hovertexts.append(title)

#map the earthquakes
data = [{
	'type': 'scattergeo',
	'lon': lons,
	'lat': lats,
	'text': hovertexts, #this adds text (from the title key/value) when you hover over an earthquakes spot 
	'marker': {
		'size': [5*mag for mag in mags], #this sets the sie of each marker, so 5*mag because mag is an integer
		'color': mags, #this sets what is being coloured and what to scale to
		'colorscale': 'Viridis', #sets available colourscale (viridis is yellow to dark blue)
		'reversescale': True, #reverse the colour scheme from dark blue - yellow to yellow - dark blue
		'colorbar': {'title': 'Magnitude'}, #this gives the colour key on the side of the map a title
	},
		}]

my_layout = Layout(title='Global Earthquakes')
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthwquakes.html')