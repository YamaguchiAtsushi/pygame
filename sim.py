import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
import math
class Robot:
    def __init__(self, x, y, yaw, v, w, dt, color):
        self. x = x
        self.y = y
        self.yaw = yaw
        self.v = v
        self.w = w
        self.dt = dt
        self.color = color

    def noise(self):
        self.x += random.uniform(-2, 2)
        self.y += random.uniform(-2, 2)

    def update(self):
        self.x += self.v * math.cos(self.yaw) * self.dt
        self.y += self.v * math.sin(self.yaw) * self.dt
        self.yaw += self.w * self.dt
        # self.noise()

robot1 = Robot(x = 0, y = 0, yaw = 0, v = 1000, w = 10, dt = 0.01, color = "red")

plot_size_x = 100
plot_size_y = 100
sim_time_step = 0.1

while True:
    plt.clf()
    plt.xlim(-500, 500)
    plt.ylim(-500, 500)
    plt.grid(which='major', color='black', linestyle='-')
    # plt.grid(which='minor', color='black', linestyle='-')
    # for i in range(len(self.landmarks)):
    #     plt.plot(self.landmarks[i][0], self.landmarks[i][1], marker='o', color='black', markersize=30)
    # for i in range(len(measurements)):
    #     if measurements[i][0] > 0.0:
    #         mx = measurements[i][0] * math.cos(yaw + measurements[i][1]) + x
    #         my = measurements[i][0] * math.sin(yaw + measurements[i][1]) + y
    #         plt.plot(mx, my, marker='o', color='red', markersize=20)
    # plt.plot(self.gt_x, self.gt_y, marker='o', color='black', markersize=30)
    robot1.update()
    robot1.noise()
    plt.plot(robot1.x, robot1.y, marker='o', color='green', markersize=20)
    plt.pause(sim_time_step)
