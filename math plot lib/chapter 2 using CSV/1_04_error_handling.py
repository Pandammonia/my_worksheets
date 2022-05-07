import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename =  'data/death_valley_2018_simple.csv'
with open(filename) as f: 
	reader = csv.reader(f) #reader variable = file opened with csv reader
	header_row = next(reader) #header row is the next row in the file 
	

	dates, highs, lows = [], [], []
	for row in reader:
		current_date = datetime.strptime(row[2], '%Y-%m-%d') 
		try:
			high = int(row[4]) # 
			low = int(row[5])
		except ValueError:
			print(f"Missing data for {current_date}")
		else:
			dates.append(current_date) 
			highs.append(high) # s
			lows.append(low)


#plot in high temps and dates
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha = 0.5) #alpha sets transparency where 1 is opaque
ax.plot(dates, lows, c='blue', alpha = 0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha = 0.1) #plt.fill_between takes argument(x, y, y, and fills with colour/alpha)
#format plot
plt.title("Daily high and low temperatures - 2018", fontsize=24)
plt.xlabel('', fontsize = 16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F):", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()