import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.ylabel("Some Numbers")
plt.show()

plt.plot([1,2,3,4], [1,4,9,16])
plt.ylabel("X Squared")
plt.show()

plt.plot([1,2,3,4], [1,4,9,16], "ro")
plt.ylabel("X Squared")
plt.axis([0,6,0,20])
plt.show()
