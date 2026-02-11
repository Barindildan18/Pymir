from imports import *
from environment import *

robot_position_x = 80
robot_position_y = 80 * 4
robot_width = 80
robot_height = 80

def draw_robot():
	pygame.draw.rect(screen, (0, 255, 0), (robot_position_x, robot_position_y, robot_width, robot_height))

def left(times):
	for i in range(1, times):
		pygame.draw.rect(screen, (0, 255, 0), (robot_position_x - (step * i), robot_position_y, robot_width, robot_height))
def right(times):
	for i in range(1, times):
		pygame.draw.rect(screen, (0, 255, 0), (robot_position_x + (step * i), robot_position_y, robot_width, robot_height))
def down(times):
	for i in range(1, times):
		pygame.draw.rect(screen, (0, 255, 0), (robot_position_x, robot_position_y + (step * i), robot_width, robot_height))
def up(times):
	for i in range(1, times):
		pygame.draw.rect(screen, (0, 255, 0), (robot_position_x, robot_position_y - (step * i), robot_width, robot_height))


