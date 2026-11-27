import matplotlib.pyplot as plt

x = [2005,2010,2015,2020,2025]
y = [5,7,13,4,17]
z = [6,3,8,3,9]

plt.plot(x,y,z,marker="p",mfc="r",markersize="10",lw="3",linestyle="-.",color="green",mec="black")

plt.show()