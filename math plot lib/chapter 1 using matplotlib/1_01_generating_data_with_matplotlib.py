import matplotlib.pyplot as plt 
encoding = 'raw_unicode_escape'
input_values = [1, 2, 3, 4, 5] #this is given so the graph knows what to plot on the X axis, (default strts at 0)
squares = [1, 4, 9, 16, 25]
plt.style.use('ggplot') #this changes the style of the graph to see available styles open a terminal and enter
#import matplotlib.pyplot as plt, plt.style.available

fig, ax = plt.subplots() #variable fig represents the entirety of plots, ag represents a single plot (for ax in fig)
ax.plot(input_values, squares, linewidth=3) #plot plots the data given 
#set charts title and label the axis
ax.set_title("Square numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#set the size of tick labels
ax.tick_params(axis='both', labelsize=10) # changes the size of ticks running along the x/y axis
plt.show()

