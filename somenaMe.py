from matplotlib import markers
import matplotlib.pyplot as plt
import numpy as np

# a = (v-u)/t - A = acceleration, v = initial velocity, u = initial velocity, t = time

#class Trajectory:
#    def __init__(self, x, x_2, y, y_2):
#        self.x = x
#        self.x_2 = x_2
#        self.y = y
#        self.y_2 = y_2
#
#    def plot(self):
#        xpoints = np.array([self.x, self.x_2])
#        ypoints = np.array([self.y, self.y_2])
#
#        plt.plot(xpoints, ypoints, marker="*", markersize=10, color="red")
#        plt.title("Trajectory")
#        plt.xlabel("Feet")
#        plt.ylabel("Feet")
#        plt.grid()
#        plt.show()

mo = 1500
q = 2.5
u = 6000
vo = 0
g = 9.81
x0 = 0
t = np.arange(0, int(mo / q))


def velocity(t):
    return vo + u * (np.long(mo / (mo - q * t)) - g * t)


def x(t):
    return (
        x0
        + vo * t
        - 0.5 * g * t**2
        + u * t * np.log(mo)
        + (u / q) * ((mo - q * t) * np.log(mo - q * t) + q * t - mo * np.log(mo))
    )


if __name__ == "__main__":
    # Trajectory(1, 8, 3, 10).plot()
    plt.plot(x(t), t)
    plt.title("Trajectory")
    plt.xlabel("Feet")
    plt.ylabel("Feet")
    plt.grid()
    plt.show()
