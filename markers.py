import matplotlib.pyplot as plt

x = [2005,2010,2015,2020,2025]
y = [5,7,13,4,17]

plt.plot(x,y,marker="p",mfc="r",markersize="10",lw="3",linestyle="-.",color="green",mec="black")

plt.show()