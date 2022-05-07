import csv
from datetime import datetime
	import matplotlib.pyplot as plt

	filename = 'data/sitka_weather_2018_simple.csv'
	with open(filename) as f: 
	reader = csv.reader(f) #reader variable = file opened with csv reader
	header_row = next(reader) #header row is the next row in the file 
	

	dates, highs = [], []
	for row in reader:
		current_date = datetime.strptime(row[2], '%Y-%m-%d') #we use strptime to get the dates from the file
		high = int(row[5]) # see previous
		dates.append(current_date) #add cufrrent date to list
		highs.append(high) # see previous

print(highs)

#plot in high temps and dates
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot (dates, highs, c='red')

#format plot
plt.title("Daily high temperatures - 2018", fontsize=24)
plt.xlabel('', fontsize = 16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F):", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()