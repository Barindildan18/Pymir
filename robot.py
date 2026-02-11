from imports import *
from properties import *

robot_surface = pygame.Surface((robot_size, robot_size))
robot = robot_surface.get_rect()
robot.topleft = start

def draw_robot():
	time.sleep(time_interval)
	screen.fill(background_color)
	screen.blit(robot_surface, robot)
	robot_surface.fill(robot_color)
def left():
	robot.x -= step
def right():
	robot.x += step
def up():
	robot.y -= step
def down():
	robot.y += step
def stop():
	robot.x = robot.x
	robot.y = robot.y
