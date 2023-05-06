import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
import math
class Robot:
    def __init__(self, x, y, yaw, v, w, dt):
        self. x = x
        self.y = y
        self.yaw = yaw
        self.v = v
        self.w = w
        self.dt = dt

    def noise(self):
        self.x += random.uniform(-2, 2)
        self.y += random.uniform(-2, 2)

    def update(self):
        self.x += self.v * math.cos(self.yaw) * self.dt
        self.y += self.v * math.sin(self.yaw) * self.dt
        self.yaw += self.w * self.dt

        # self.noise()

    def plot(self, robot_color):
        sim_time_step = 0.001

        #plt.clf()
        plt.xlim(-100, 100)
        plt.ylim(-100, 100)
        plt.grid(which='major', color='black', linestyle='-')
        plt.plot(self.x, self.y, marker='o', color = robot_color, markersize=5)
        plt.pause(sim_time_step)

def main():
    robot1 = Robot(x = 0, y =-50, yaw = 0, v = 500, w = 10, dt = 0.01)
    robot2 = Robot(x = 0, y =-50, yaw = 0, v = 500, w = 10, dt = 0.01)

    while True:
        robot1.plot("red")
        robot1.update()
        robot1.noise()
        robot2.plot("blue")
        robot2.update()



if __name__ == "__main__":
    main()
