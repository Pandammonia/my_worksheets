import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f: 
	reader = csv.reader(f) #reader variable = file opened with csv reader
	header_row = next(reader) #header row is the next row in the file 
	

	dates, highs, lows = [], [], []
	for row in reader:
		current_date = datetime.strptime(row[2], '%Y-%m-%d') 
		high = int(row[5]) # 
		low = int(row[6])
		dates.append(current_date) 
		highs.append(high) # s
		lows.append(low)

print(highs)

#plot in high temps and dates
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')
ax.plot(dates, lows, c='blue')

#format plot
plt.title("Daily high and low temperatures - 2018", fontsize=24)
plt.xlabel('', fontsize = 16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F):", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()