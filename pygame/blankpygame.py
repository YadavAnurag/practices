try:
	import pygame, sys
	from pygame.locals import *
except ImportError as e:
	print(e)


pygame.init()
DISPLAYSURF = pygame.display.set_mode((600, 300))
pygame.display.set_caption('Hello World')

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()
	

