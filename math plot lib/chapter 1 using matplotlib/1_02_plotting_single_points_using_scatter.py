import matplotlib.pyplot as plt 

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(2,4, s=200) #calls scatter and sets the dot size to 200 x = 2 y = 4

#set chart title and axis labels
ax.set_title("Square numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 10)
ax.set_ylabel("Square of Value", fontsize = 14)

#set size of tick labels
ax.tick_params(axis = 'both', which='major', labelsize = 14)


plt.show()