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
        # self.yaw += random.uniform(-0.5, 0.5)

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

class Landmark:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def plot(self, landmark_color):
        sim_time_step = 0.001

        #plt.clf()
        # plt.xlim(-100, 100)
        # plt.ylim(-100, 100)
        # plt.grid(which='major', color='black', linestyle='-')
        plt.plot(self.x, self.y, marker='o', color = landmark_color, markersize=5)
        plt.pause(sim_time_step)

class Camera:
    def __init__(self, robot, landmark):
        self.robot = robot
        self.landmark = landmark

    def calc(self):
        self.l_x = self.landmark.x - self.robot.x
        self.l_y = self.landmark.y - self.robot.y
        self.distance = math.sqrt(self.l_x ** 2 + self.l_y ** 2)
        self.arg = math.atan2(self.l_y, self.l_x) - self.robot.yaw
        # while self.arg >= np.pi:
        #     self.arg -= 2*np.pi
        # while self.arg < np.pi:
        #     self.arg += 2*np.pi

    def plot(self, camera_color):
        sim_time_step = 0.001
        plt.plot((self.robot.x, self.robot.x + self.distance * math.cos(self.arg)), (self.robot.y,  self.robot.y + self.distance * math.sin(self.arg)), color = camera_color, markersize=5)
        print(self.arg)
        # plt.plot((self.robot.x, self.landmark.x), (self.robot.y,  self.landmark.y), color = camera_color, markersize=5)

        plt.pause(sim_time_step)

def main():
    robot1 = Robot(x = 0, y =-50, yaw = 0, v = 500, w = 10, dt = 0.01)
    robot2 = Robot(x = 0, y =-50, yaw = 0, v = 500, w = 10, dt = 0.01)
    landmark1 = Landmark(-80, -70)
    landmark2 = Landmark(80, -60)
    landmark3 = Landmark(-50, 90)

    landmark1.plot("green")
    landmark2.plot("green")
    landmark3.plot("green")

    camera1 = Camera(robot1, landmark1)
    camera2 = Camera(robot1, landmark2)
    camera3 = Camera(robot1, landmark3)

    while True:

        robot1.plot("red")
        robot1.update()
        robot1.noise()
        robot2.plot("blue")
        robot2.update()
        camera1.calc()
        camera2.calc()
        camera3.calc()
        camera1.plot("black")
        camera2.plot("black")
        camera3.plot("black")



if __name__ == "__main__":
    main()
