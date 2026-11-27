import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")

data.plot()

plt.show()


# import matplotlib.pyplot as plt

# x = [0,5,10]
# y = [1,5,1]
# z = [1,1,1,1,1,1,1,1,1,1,1]
# plt.plot(x,y,z,marker="p",mfc="r",markersize="10",lw="3",linestyle="-.",color="green",mec="black")

# plt.show()