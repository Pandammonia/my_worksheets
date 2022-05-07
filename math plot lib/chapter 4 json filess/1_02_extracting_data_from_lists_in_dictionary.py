import json
#Explore structure of data
filename = 'data/eq_data_1_day_m1.json' #open json file as filename
with open(filename) as f:
	all_eq_data = json.load(f) #store all data in all eq data

all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts)) 

mags, lons, lats, = [], [], [] 
for eq_dict in all_eq_dicts: #create loop for all of our data
	mag = eq_dict['properties']['mag'] #magnitude is under each dictioanry in [properties] [mag]
	lon = eq_dict['geometry']['coordinates'][0]
	lat = eq_dict['geometry']['coordinates'][1]
	mags.append(mag)
	lons.append(lon)
	lats.append(lat)

print(mags[:10])
print(lons[:5])
print(lats[:5])