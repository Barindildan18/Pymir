from imports import *
from environment import *
from robot import *

pygame.init()
pygame.display.set_caption("РОБОТ")

is_running = True

while is_running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			is_running = False
	
	pygame.draw.rect(screen, (38, 38, 38), (0, 0, 640, 640))
	draw_walls()
	draw_robot()
	pygame.display.update()
