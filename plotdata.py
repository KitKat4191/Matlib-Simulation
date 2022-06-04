import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the csv file
#data = pd.read_csv('data.csv')

# Print it out if you want

dataArray = np.genfromtxt('data.csv', delimiter=',', names=True)
#    dataArray

plt.figure()
for col_name in dataArray.dtype.names:
    plt.plot(dataArray[col_name], label=col_name)
plt.legend()
plt.show()


# if __name__ == "__main__":
#    plt.plot(data)
#    plt.title("yes")
#    plt.xlabel("Feet")
#    plt.ylabel("Feet")
#    plt.grid()
#    plt.show()
