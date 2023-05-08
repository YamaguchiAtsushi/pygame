from sim import *

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
            self.x += random.gauss(0, 100 * self.noise)
            self.y += random.gauss(0, 100 * self.noise)
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

def main():
    particle = Particle(x = 0, y =-50, yaw = 0, v = 500, w = 10, dt = 0.01, noise = 0.001)

    while True:
        particle.update()
        particle.plot("red")
        print(particle.x, particle.y)

if __name__ == "__main__":
    main()