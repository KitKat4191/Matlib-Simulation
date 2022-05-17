from matplotlib import markers
import matplotlib.pyplot as plt
import numpy as np

class Trajectory:
    def __init__(self, x, x_2, y , y_2):
        self.x = x
        self.x_2 = x_2
        self.y = y
        self.y_2 = y_2
        
        
    def plot(self):
        xpoints = np.array([self.x, self.x_2])
        ypoints = np.array([self.y, self.y_2])
        
        plt.plot(xpoints, ypoints, marker = '*', markersize = 10, color = 'red')
        plt.title('Trajectory')
        plt.xlabel('Feet')
        plt.ylabel('Feet')
        plt.grid()
        plt.show()
        


def printHello():
    print("Hello world!")


if __name__ == "__main__":
    Trajectory(1, 8, 3, 10).plot()
