import matplotlib.pyplot as plt
input_values=[1,2,3,4,5]
squares=[1,4,9,16,25]
cubes=[1,8,27,64,125]
f_power=[1,32,243,1024,3125]
plt.plot(input_values,squares,linewidth=5,c="red",label="squares")
plt.plot(input_values,cubes,linewidth=5,label="cubes")
plt.plot(input_values,f_power,linewidth=5,label="f_power")
plt.legend()
plt.xlim(2,4,5)
plt.show()
