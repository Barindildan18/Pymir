from imports import *
from properties import *

step = 80

def draw_walls():
	row_index = 0
	for row in placement:
		row_index += 1
		wall_index = 0
		for wall in row:
			wall_index += 1
			if wall[0] and wall[1] == 'H':
				pygame.draw.rect(screen, wall_color, (step * wall_index, step * (row_index-1), wall_width, wall_height))
			elif wall[0] and wall[1] == 'V':
				pygame.draw.rect(screen, wall_color, (step * wall_index, step * (row_index-1), wall_height, wall_width))

