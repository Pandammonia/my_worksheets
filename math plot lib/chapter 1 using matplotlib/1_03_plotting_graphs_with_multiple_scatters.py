import matplotlib.pyplot as plt
x_val = [1, 2, 3, 4, 5]
y_val = [1, 4, 9, 16, 25]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_val, y_val, s=100) 

ax.set_title("Square numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 16)
ax.set_ylabel("Square of value", fontsize = 16)
ax.tick_params(axis='both', which='major', labelsize=16)
plt.show()