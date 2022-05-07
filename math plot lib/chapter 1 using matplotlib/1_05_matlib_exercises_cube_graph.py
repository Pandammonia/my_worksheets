import matplotlib.pyplot as plt

x_val = [1,2,3,4,5]
y_val = [1,8,27,64,125] 

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_val, y_val, s=15)
ax.set_title("Cubes", fontsize =24)
ax.set_xlabel("Value", fontsize=18)
ax.set_ylabel("Cube of value", fontsize=18)
ax.tick_params(axis='both', which='major', labelsize=16) 
plt.show()