from imports import *
from environment import *
from robot import *
from commands import move

pygame.init()
pygame.display.set_caption("РОБОТ")

is_running = True
while is_running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			is_running = False
	draw_robot()
	pygame.display.flip()
