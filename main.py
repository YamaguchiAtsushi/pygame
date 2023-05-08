from sim import *

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
    camera1.plot("pink")
    camera2.plot("pink")
    camera3.plot("pink")