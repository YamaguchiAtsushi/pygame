import random
import pygame
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

    def draw(self, screen):
        radius = 3
        pygame.draw.circle(screen, pygame.Color(self.color), (self.x, self.y), radius)



def main():
    pygame.init()
    width, height = 900, 600
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    robot1 = Robot(x = 450, y = 300, yaw = 0, v = 100, w = 1, dt = 0.01, color = "red")
    robot2 = Robot(x = 450, y = 300, yaw = 0, v = 100, w = 1, dt = 0.01, color = "blue")

    screen.fill(pygame.Color("white"))

    while True:
        frames_per_second = 60
        clock.tick(frames_per_second)
        robot1.update()
        robot1.noise()
        robot1.draw(screen)
        robot2.update()
        robot2.draw(screen)
        pygame.display.update()

    robot_list = []

    while True:

        robot_list.append(robot)
        robot.update()
        screen.fill(pygame.Color("black"))
        for robot in robot_list:
            robot.draw(screen)
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()
