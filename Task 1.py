import matplotlib.pyplot as plt
cubic = []
numx = list(range(1,5001))
#First five cubic [1,8,27,64,125]
numy = [x**3 for x in numx]
plt.scatter(numx,numy,c=numy,cmap = plt.cm.Blues, edgecolor = 'red', s=2)
plt.scatter('x', 'y')
#cmap = plt.cm.Blues,
#set the range for each axis
plt.axis([0,5500,0,5500000])
plt.plot(cubic, marker='o', linewidth=5)
plt.plot(numx, numy, marker = '*')
plt.title("Series of Numbers")
plt.xlabel("x coordinate")
plt.ylabel("y coordinate")
plt.legend(["squares", "numx and numy"])
plt.show()
plt.savefig('d\\bleh.png')
plt.savefig("d\\bleh2.npg", bbox_inches = 'tight')
