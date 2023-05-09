from sim import *
from numpy.random import normal
import math

class Particle():
    def __init__(self, x, y, yaw, v, w, dt, noise):
        self.x = x
        self.y = y
        self.yaw = yaw
        self.v = v
        self.w = w
        self.dt = dt
        self.particles = []
        self.particles.append([self.x, self.y, self.yaw])
        self.particle_num = 100
        self.noise = noise

    def update(self):
        self.x += self.v * math.cos(self.yaw) * self.dt
        self.y += self.v * math.sin(self.yaw) * self.dt
        self.yaw += self.w * self.dt
        self.noise += 0.0001
        for i in range(self.particle_num):
            self.x += random.gauss(0, (100 + 0.1 * i) * self.noise)
            self.y += random.gauss(0, (100 + 0.1 * i) * self.noise)
            self.yaw += random.gauss(0, 0.0001)
            self.particles.append([self.x, self.y, self.yaw])
            # print(i, "=", self.particles)


    def plot(self, particle_color):
        sim_time_step = 0.01

        plt.clf()
        plt.xlim(-100, 100)
        plt.ylim(-100, 100)
        plt.grid(which='major', color='black', linestyle='-')
        for i in range(self.particle_num):
            plt.plot(self.particles[i][0], self.particles[i][1], marker = 'o', color = particle_color, markersize = 1)
            # plt.arrow(x=self.particles[i][0], y=self.particles[i][1], dx=0.5*math.cos(self.particles[i][2]), dy=0.5*math.sin(self.particles[i][2]), width=0.05, head_width=0.25, head_length=0.15, length_includes_head=True, color='blue')
        plt.pause(sim_time_step)
        del self.particles[:]


class Landmark:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def plot(self, landmark_color):
        sim_time_step = 0.01
        plt.plot(self.x, self.y, marker='o', color = landmark_color, markersize=5)
        plt.pause(sim_time_step)

class Camera:
    def __init__(self, particle, landmark):
        self.particle = particle
        self.landmark = landmark

    def calc(self):
        measure = []
        self.dx = self.landmark.x - self.particle.x
        self.dy = self.landmark.y - self.particle.y
        self.dl = normal(math.sqrt(self.dx * self.dx + self.dy * self.dy), 0.04) #add noise
        # if self.dl <= 100: #must be change value
        #     self.dyaw = normal(math.atan2(self.dy, self.dx) - self.particle.yaw, 0.04)
        self.dyaw = normal(math.atan2(self.dy, self.dx), 0.04)
        measure.append([self.dl, self.dyaw])
        return measure

    def plot(self, camera_color):
        sim_time_step = 0.001
        plt.plot((self.particle.x, self.particle.x + self.dl * math.cos(self.dyaw)), (self.particle.y,  self.particle.y + self.dl * math.sin(self.dyaw)), color = camera_color, markersize=10)
        plt.pause(sim_time_step)



def main():
    plt.clf()
    plt.xlim(-100, 100)
    plt.ylim(-100, 100)
    plt.grid(which='major', color='black', linestyle='-')

    particle = Particle(x = 0, y =-50, yaw = 0, v = 500, w = 10, dt = 0.01, noise = 0.001)

    landmark1 = Landmark(-80, -70)
    landmark2 = Landmark(80, -60)
    landmark3 = Landmark(-50, 90)

    camera1 = Camera(particle, landmark1)
    camera2 = Camera(particle, landmark2)
    camera3 = Camera(particle, landmark3)



    while True:
        particle.update()
        particle.plot("red")
        # print(particle.x, particle.y)
        # landmark1.plot("green")
        # landmark2.plot("green")
        # landmark3.plot("green")
        landmark1.plot("green")
        landmark2.plot("green")
        landmark3.plot("green")
        camera1.calc()
        camera2.calc()
        camera3.calc()
        camera1.plot("pink")
        camera2.plot("pink")
        camera3.plot("pink")


if __name__ == "__main__":
    main()