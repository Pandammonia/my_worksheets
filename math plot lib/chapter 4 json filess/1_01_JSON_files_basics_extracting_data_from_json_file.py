import json
#Explore structure of data
filename = 'data/eq_data_1_day_m1.json' #open json file as filename
with open(filename) as f:
	all_eq_data = json.load(f) #store all data in all eq data

all_eq_dicts = all_eq_data['features'] #all dictionarie are located under key "features"
print(len(all_eq_dicts)) #print the length of this list here to make sure we have a list of 158 earthquakes

mags = [] #get magnitudes
for eq_dict in all_eq_dicts: #create loop for all of our data
	mag = eq_dict['properties']['mag'] #magnitude is under each dictioanry in [properties] [mag]
	mags.append(mag) #add the magnitude to the list

print(mags[:10])