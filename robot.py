from imports import *
from environment import *
from properties import *


#def left():
	
		
def right(times):
	for i in range(times):
		pygame.draw.rect(screen, (0, 255, 0), (robot_pos_x + (step * (i + 1)), robot_pos_y, robot_width, robot_height))
def down(times):
	for i in range(times):
		pygame.draw.rect(screen, (0, 255, 0), (robot_pos_x, robot_pos_y + (step * (i + 1)), robot_width, robot_height))
def up(times):
	for i in range(times):
		pygame.draw.rect(screen, (0, 255, 0), (robot_pos_x, robot_pos_y - (step * (i + 1)), robot_width, robot_height))


def draw_robot():
	pygame.draw.rect(screen, (0, 255, 0), (start[0], start[1], robot_width, robot_height))

